// import React, {Component} from "react";
// import {StyleSheet, View, SafeAreaView} from "react-native";
// import Ionicons from 'react-native-vector-icons/Ionicons';
// import shortid from "shortid";
// import {Autocomplete, withKeyboardAwareScrollView} from "react-native-dropdown-autocomplete";
// import URL from '../api/ApiURL';
// import Colors from '../ColorCodes/Colors';
// import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
// class MyDropDown extends Component {
//   handleSelectItem(item, index) {
//     const {onDropdownClose} = this.props;
//     onDropdownClose();
//     console.log(item);
//   }

//   render() {
//     const autocompletes = [...Array(10).keys()];

//     const apiUrl = URL+"/product/product_list/";

//     const {scrollToInput, onDropdownClose, onDropdownShow} = this.props;

//     return (
//       <View style={styles.autocompletesContainer}>
//         <SafeAreaView>
//           {autocompletes.map(() => (
//             <Autocomplete
//               key={shortid.generate()}
//               style={styles.input}
//               scrollToInput={ev => {}}
//               handleSelectItem={(item, id) => this.handleSelectItem(item, id)}
//               onDropdownClose={() => onDropdownClose()}
//               onDropdownShow={() => onDropdownShow()}
//               renderIcon={() => (
//                 <Ionicons name="ios-add-circle-outline" size={20} color="#c7c6c1" style={styles.plus} />
//               )}
//               fetchDataUrl={apiUrl}
//               minimumCharactersCount={2}
//               highlightText
//               highLightColor={Colors.themeColor}
//               valueExtractor={item => item.name}
//               //rightContent
//               //rightTextExtractor={item => item.properties}
//             />
//           ))}
//         </SafeAreaView>
//       </View>
//     );
//   }
// }
// const styles = StyleSheet.create({
//   autocompletesContainer: {
//     paddingTop: 0,
//     zIndex: 1,
//     width: "100%",
//     paddingHorizontal: 8,
//   },
//   input: {maxHeight: 40},
//   inputContainer: {
//     display: "flex",
//     flexShrink: 0,
//     flexGrow: 0,
//     flexDirection: "row",
//     flexWrap: "wrap",
//     alignItems: "center",
//     borderBottomWidth: 1,
//     borderColor: "#c7c6c1",
//     paddingVertical: 13,
//     paddingLeft: 12,
//     paddingRight: "5%",
//     width: "100%",
//     justifyContent: "flex-start",
//   },
//   container: {
//     flex: 1,
//     backgroundColor: "#ffffff",
//   },
//   plus: {
//     position: "absolute",
//     left: 15,
//     top: 10,
//   },
// });

// export default MyDropDown

//Example of React Native AutoComplete Input
//https://aboutreact.com/example-of-react-native-autocomplete-input/

//import React in our code
import React, {useState, useEffect} from 'react';

//import all the components we are going to use
import {
  SafeAreaView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import URL from '../api/ApiURL';
//import Autocomplete component
import Autocomplete from 'react-native-autocomplete-input';

const MyDropDown = () => {
  const [films, setFilms] = useState([]);
  const [filteredFilms, setFilteredFilms] = useState([]);
  const [selectedValue, setSelectedValue] = useState({});

  useEffect(() => {
    fetch(URL+'/product/product_list/')
    .then((response) => response.json())
    .then((responseJson) => {
       // const {results: films} = json;
        setFilms(responseJson);
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
      const regex = new RegExp(`${query.trim()}`, 'i');
      //setting the filtered film array according the query from the input
      setFilteredFilms(films.filter((film) => film.name.search(regex) >= 0));
    } else {
      //if the query is null then return blank
      setFilteredFilms([]);
    }
  };

  return (
    <SafeAreaView style={{flex: 1}}>
      <View style={styles.container}>
        <Autocomplete
          autoCapitalize="none"
          autoCorrect={false}
          containerStyle={styles.autocompleteContainer}
          //data to show in suggestion
          data={filteredFilms}
          //default value if you want to set something in input
          defaultValue={
            JSON.stringify(selectedValue) === '{}' ? '' : selectedValue.name
          }
          /*onchange of the text changing the state of the query which will trigger
          the findFilm method to show the suggestions*/
          onChangeText={(text) => findFilm(text)}
          placeholder="Add Item"
          //highlightTextColor="red"
          renderItem={({item}) => (
            //you can change the view you want to show in suggestion from here
            <TouchableOpacity
              onPress={() => {
                setSelectedValue(item);
                setFilteredFilms([]);
              }}>
              <Text style={styles.itemText}>{item.name}</Text>
            </TouchableOpacity>
          )}
        />
        {/* <View style={styles.descriptionContainer}>
          {films.length > 0 ? (
            <>
              <Text style={styles.infoText}>Selected Data</Text>
              <Text style={styles.infoText}>
                {JSON.stringify(selectedValue)}
              </Text>
            </>
          ) : (
            <Text style={styles.infoText}>Enter The Film Title</Text>
          )}
        </View> */}
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#F5FCFF',
    // flex: 1,
    padding: 16,
    // marginTop: 40,
  },
  autocompleteContainer: {
    backgroundColor: '#ffffff',
    borderWidth: 0,
  },
  descriptionContainer: {
    flex: 1,
    justifyContent: 'center',
  },
  itemText: {
    fontSize: 15,
    paddingTop: 5,
    paddingBottom: 5,
    margin: 2,
  },
  infoText: {
    textAlign: 'center',
    fontSize: 16,
  },
});

export default MyDropDown;
