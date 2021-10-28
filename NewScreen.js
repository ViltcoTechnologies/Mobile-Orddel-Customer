import React, { useState, useEffect } from "react";

//import all the components we are going to use
import {
  SafeAreaView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
ScrollView
} from "react-native";

//import Autocomplete component
import Autocomplete from "react-native-autocomplete-input";

const NewScreen = () => {
  const [films, setFilms] = useState([]);
  const [filteredFilms, setFilteredFilms] = useState([]);
  const [selectedValue, setSelectedValue] = useState({});

  useEffect(() => {
    fetch("http://52.14.120.54:8069/get_city_ids")
      .then((res) => res.json())
      .then((json) => {
        console.log(json)
        // const { films } = json;
        setFilms(json);
        console.log(films);
        //setting the data in the films state
      })
      .catch((e) => {
        alert(e);
      });
  }, []);

  const findFilm = (query) => {
    //method called everytime when we change the value of the input
    if (query) {
      //making a case insensitive regular expression to get similar value from the film json
      const regex = new RegExp(`${query.trim()}`, "i");
      //setting the filtered film array according the query from the input
      setFilteredFilms(films.filter((film) => film.name.search(regex) >= 0));
    } else {
      //if the query is null then return blank
      setFilteredFilms([]);
    }
  };

  return (
    // <SafeAreaView style={{ flex: 1 }}>
      <View style={styles.container}>
        <ScrollView>
        <Autocomplete
          autoCapitalize="none"
          autoCorrect={false}
          containerStyle={styles.autocompleteContainer}

          //data to show in suggestion
          data={filteredFilms}
          //default value if you want to set something in input
          defaultValue={
            JSON.stringify(selectedValue) === "{}" ? "" : selectedValue.name
          }
          /*onchange of the text changing the state of the query which will trigger
          the findFilm method to show the suggestions*/
          onChangeText={(text) => findFilm(text)}
          placeholder="Enter the film title"
          renderItem={({ item }) => (
            //you can change the view you want to show in suggestion from here
            <TouchableOpacity
              onPress={() => {
                setSelectedValue(item);
                setFilteredFilms([]);
              }}
            >
              <Text>{item.name}</Text>
            </TouchableOpacity>
          )}
        />
        <View >
          {films.length > 0 ? (
            <>
              <Text >Selected Data</Text>
              {/* <Text >
                {JSON.stringify(selectedValue)}
              </Text> */}
            </>
          ) : (
            <Text >Enter The Film Title</Text>
          )}
        </View>
        <Text> Title: {JSON.stringify(selectedValue.name)} </Text>
        </ScrollView>
      </View>
    // {/* </SafeAreaView> */}
  );
};

const styles = StyleSheet.create({

    container:{
        flex:1,
        justifyContent:'center',
        //alignItems:'center'
        //alignContent:'flex-end',
        alignSelf:'center'

    }
})

export default NewScreen ;