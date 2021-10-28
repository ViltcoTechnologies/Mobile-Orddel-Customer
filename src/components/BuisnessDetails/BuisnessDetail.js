import React from "react";
import { useState, useEffect } from "react";
import {
  Image,
  ScrollView,
  ActivityIndicator,
  FlatList,
  TouchableHighlight,
  TouchableOpacity,
  StyleSheet,
  LogBox,
  BackHandler
} from "react-native";

import {
  Container,
  Header,
  Spinner,
  Card,
  CardItem,
  Title,
  Thumbnail,
  Content,
  Text,
  Button,
  Left,
  Body,
  Right,
  View,
} from "native-base";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import AntDesign from "react-native-vector-icons/AntDesign";
import { useIsFocused } from "@react-navigation/native";
import { useRoute, useFocusEffect } from "@react-navigation/native";
//import ViewShot from "react-native-view-shot";
import Colors from "../../ColorCodes/Colors";
import Ionicons from "react-native-vector-icons/Ionicons";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import URL from "../../api/ApiURL";
import { useSelector, useDispatch } from "react-redux";
import MyHeader from "../../components/MyHeader";

//import * as ApiAction from "../../store/actions/ApiData";
import * as BusinessDate from "../../store/actions/BusinessDate";

const BuisnessDetail = ({ navigation,route }) => {

  useFocusEffect(
    React.useCallback(() => {
      const backAction = () => {
        navigation.navigate("Dashboard")
        
        return true;
      };
  
      const backHandler = BackHandler.addEventListener(
        "hardwareBackPress",
        backAction
      );
  
      return () => backHandler.remove();
    }, [route])
  );





  const ClientId = useSelector((state) => state.ApiData.ClientId);
  //   const { Shipper_ID } = route.params;




  const dispatch = useDispatch();
  const isFocused = useIsFocused();

  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState([]);
  const [list, setList] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    LogBox.ignoreLogs(["VirtualizedLists should never be nested"]);
  }, []);
  useEffect(() => {
    //   console.log("hi---------------")
    LogBox.ignoreLogs([
      "Can't perform a React state update on an unmounted component",
    ]);

    setIsLoading(true);
    fetch(URL + "/client_app/list_business/client/" + ClientId + "/")
      // fetch(URL+'/client_app/clients_list/33/')
      .then((response) => response.json())
      .then((responseJson) => {
        console.log("Buisness Detail:", responseJson);
        
        setData(responseJson.client_businesses);
        if (responseJson.client_businesses == "") {
          setIsLoading(false);
          setLoading(true);
        } else {
          setLoading(false);
        }
        setIsLoading(false);
        
      })
      .catch((error) => console.error(error));
    
  }, [isFocused]);

  return (
    <View style={{ flex: 1, height: "100%" }}>
      {/* <MyHeader name="BUSINESS DETAIL" nav={navigation} /> */}

      <View style={{ marginTop: 10 }}>
        <TouchableOpacity
          style={styles.uploadButton}
          activeOpacity={0.7}
          onPress={() => navigation.navigate("NewBuisnessDetail")}
        >
          <Text style={styles.uploadButtonText}>Add New Business</Text>
        </TouchableOpacity>
      </View>
      {loading && (
        <View
          style={{
            justifyContent: "center",
            alignItems: "center",
            marginTop: "20%",
          }}
        >
          <FontAwesome
            name="exclamation-circle"
            color={Colors.themeColor}
            // size={Platform.OS == "ios" ? 250 : 150}

            size={150}
          />
          <Text
            style={{
              color: Colors.themeColor,
              fontWeight: "bold",
              marginTop: 20,
              fontSize: 25,
            }}
          >
            NO RECORD
          </Text>
        </View>
      )}

      {isLoading ? (
        <Spinner color={Colors.themeColor} />
      ) : (
        (console.log("data", data),
        (
          <Content>
            <View style={{ marginTop: 10 }}>
              <FlatList
                data={data}
                inverted={true}
                showsVerticalScrollIndicator={false}
                style={{ alignSelf: "center", padding: 10 }}
                // keyExtractor={item => item.index_id.toString()}
                keyExtractor={({ id }, index) => id}
                renderItem={({ item }) => (
                  <Card style={{ borderRadius: 15 }}>
                    <TouchableOpacity
                      style={{ width: "100%" }}
                      onPress={() => {
                        
                        navigation.navigate("EditBuisnessDetail", {
                          BName: item.name,
                          BAdress: item.address,
                          BNature: item.nature,
                          BType: item.type,
                          ID: item.id,
                        });
                      }}

                    >
                      {/* {console.log("Business_name",item.business_details[0]['name'])} */}
                      <View
                        style={{
                          

                          flexDirection: "column",
                         
                        }}
                      >
                        {/* <View style={{flexDirection: "column"}}> */}
                        <View style={{ flexDirection: "row" }}>
                          <View
                            style={{
                              padding: 10,
                              width: "100%",
                              justifyContent: "flex-start",
                            }}
                          >
                            <Text
                              style={{
                                fontSize: 20,
                                fontWeight: "bold",
                                color: Colors.darkRedColor,
                                //   marginTop: "4%",
                              }}
                            >
                              {item.name}
                            </Text>

                            <View
                              style={{
                                // width: 200,
                                flexDirection: "row",
                                alignItems: "center",

                                marginTop: "1.5%",
                              }}
                            >
                              <Text
                                style={{
                                  fontSize: 14,
                                  color: "grey",
                                  width: 240,
                                }}
                              >
                                {item.address}
                              </Text>
                            </View>

                            
                          </View>
                          <View style={{ alignSelf: "center" }}>
                            
                          </View>
                        </View>
                      </View>
                    </TouchableOpacity>
                  </Card>
                 
                )}
              />
            </View>
          </Content>
        ))
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  signupButtonText: {
    fontSize: 20,
    color: "#ffffff",
    fontWeight: "bold",
    textAlign: "center",
  },

  signupText: {
    fontSize: 14,
    fontWeight: "bold",
    // color:'rgba(255,255,255, 0.7)',
    color: "black",
  },

  signupButton: {
    height: 40,
    width: 300,
    backgroundColor: "#EE0202",
    justifyContent: "center",
    borderRadius: 25,
    // marginVertical: 20,
  },

  signupContianer: {
    flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
  },
  uploadButton: {
    height: 40,
    width: 300,
    borderWidth: 2,
    flexDirection: "row",
    borderColor: Colors.themeColor,
    backgroundColor: "white",
    alignSelf: "center",
    borderRadius: 25,
  },
  uploadButtonText: {
    fontSize: 20,
    marginTop: 5,
    color: Colors.themeColor,
    fontWeight: "bold",
    justifyContent: "center",
    marginLeft: "20%",
  },
});
export default BuisnessDetail;
