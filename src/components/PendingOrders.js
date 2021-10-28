import React, { Component } from "react";
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

//import ViewShot from "react-native-view-shot";
import Colors from "../ColorCodes/Colors";
import Ionicons from "react-native-vector-icons/Ionicons";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import URL from "../api/ApiURL";
import { useSelector, useDispatch } from "react-redux";
import MyHeader from "../components/MyHeader";
import { useIsFocused } from "@react-navigation/native";

import * as ApiAction from "../store/actions/ApiData";
const PendingOrders = ({ navigation, route }) => {
  const ClientId = useSelector((state) => state.ApiData.ClientId);
  const isFocused = useIsFocused();

  console.log("ClientId", ClientId);
  //   const { Shipper_ID } = route.params;
  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState([]);
  const [list, setList] = useState("");
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    LogBox.ignoreLogs(["VirtualizedLists should never be nested"]);
    LogBox.ignoreLogs(['Each child in a list should have a unique "key" prop']);
    LogBox.ignoreLogs(["Failed child context type"]);
  }, []);
  useEffect(() => {
    console.log("hi---------------");
    setIsLoading(true);
    fetch(
      URL +
        "/order/list_client_orders/?client_id=" +
        ClientId +
        "&choice=pending"
    )
      // fetch(URL+'/client_app/clients_list/33/')
      .then(async (response) => {
        let data = await response.json();
        console.log("status code", response.status);
        console.log("status code", data);
        if (response.status == 200) {
          if (data.response == "") {
            setLoading(true);
            setIsLoading(false);
          } else {
            console.log("InProgress:", data);
            setLoading(false);
            setData(data.response);
            setIsLoading(false);
          }
        } else {
          setLoading(true);
          setIsLoading(false);
        }

        // console.log("Buisness Detail:",responseJson.client_businesses[0]['name']);
        // if (json["response"] == "Record does not exist or not found") {
        //   setLoading(true);
        // } else {

        //   //console.log(json);
        // }
      })
      .catch((error) => console.error(error))
      .finally(() => setIsLoading(false));

    console.log(data);
  }, [isFocused]);

  return (
    <View style={{ flex: 1, backgroundColor: "white" }}>
      {/* <MyHeader name="PENDING ORDERS" nav={navigation} /> */}

      {/* {loading && (
        <View
          style={{
            justifyContent: "center",
            alignItems: "center",
            marginTop: "20%",
          }}
        >
          <FontAwesome name="exclamation-circle" color={Colors.themeColor} size={150} />
          <Text style={{ color: Colors.themeColor, fontWeight: "bold",marginTop:20, fontSize: 25 }}>
            NO RECORD
          </Text>
        </View>
      )} */}

      {isLoading ? (
        <Spinner color={Colors.themeColor} />
      ) : (
        // console.log("data",data),

        <Content>
          <View style={{ marginTop: 10 }}>
            {loading ? (
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
            ) : (
              <FlatList
                data={data}
                //inverted = {true}
                style={{ alignSelf: "center" }}
                showsVerticalScrollIndicator={false}
                // keyExtractor={item => item.index_id.toString()}
                keyExtractor={({ id }, index) => id}
                renderItem={({ item }) => (
                  <TouchableOpacity
                    style={{ marginTop: 5, marginBottom: 5 }}
                    onPress={() =>
                      navigation.navigate("OrderStatus", {
                        OrderBox: item.order_box,
                        OrderId: item.id,
                        Packages: item.no_of_items,
                        Quantity: item.total_quantity,
                      })
                    }
                  >
                    <View
                      style={{
                        width: "95%",
                        height: 60,
                        backgroundColor: "white",
                        alignSelf: "center",
                        borderRadius: 10,
                        flexDirection: "row",
                        shadowColor: "#000",
                        shadowOffset: { width: 0, height: 2 },
                        shadowOpacity: 0.25,
                        shadowRadius: 3.84,
                        elevation: 5,
                      }}
                    >
                      <View
                        style={{
                          width: "60%",
                          justifyContent: "center",
                          paddingLeft: 23,
                        }}
                      >
                        <Text
                          style={{
                            fontSize: 15,
                            fontWeight: "bold",
                            color: Colors.darkRedColor,
                            //   marginTop: "4%",
                          }}
                        >
                          {item.client_name}
                        </Text>
                        <Text
                            style={{
                              fontSize: 15,
                              fontWeight: "bold",
                              color: Colors.productGrey,
                              //   marginTop: "4%",
                            }}
                          >


                            {item.order_delivery_datetime.split(" ")[0]}
                          </Text>
                      </View>
                      <View
                        style={{
                          width: "40%",
                          justifyContent: "center",
                          //alignItems: "flex-end",
                          paddingLeft: 23,
                        }}
                      >
                        <View style={{ alignItems: "flex-start" }}>
                          <Text
                            style={{
                              fontSize: 12,
                              color: Colors.productGrey,
                              fontWeight: "bold",
                            }}
                          >
                            {item.no_of_items} items
                          </Text>
                        </View>
                        <Text
                          style={{
                            fontSize: 12,
                            color: Colors.productGrey,
                            fontWeight: "bold",
                          }}
                        >
                          {item.total_quantity} Packages
                        </Text>
                      </View>
                    </View>
                  </TouchableOpacity>
                  // <Card style={{ borderRadius: 15 }}>
                  //   <TouchableOpacity
                  //     style={{ width: "75%" }}
                  // onPress={()=>{
                  //     console.log("Id",item.id)
                  //     // navigation.navigate({
                  //     //     routeName: ('OrderStatus'),
                  //     //     params: {
                  //     //         OrderBox:item.order_box

                  //     //     }
                  //     //   });
                  //     navigation.navigate("OrderStatus",{OrderBox:item.order_box,OrderId:item.id,Packages:item.no_of_items});
                  // }}
                  // onPress = {() => navigation.navigate("PendingDetails" , {Due_Date : item.due_date , Invoice_Total : item.grand_total,Carrier_Name : item.carrier_company ,Load_Type : item.load_type,Origin_City : item.Origin_city,Destination_City : item.Destination_city,Delivery_Option : item.Delivery_Option,Cargo_Amount : item.Cargo_amount,Cargo_Type : item.Cargo_Type,Cargo_Product_Type : item.Cargo_Product_type,Cargo_Product_List : item.Cargo_Product_List,Booking_Status : item.booking_status})}
                  //   onPress={() =>
                  //     navigation.navigate("PaymentHistoryDetail")
                  //   }
                  //>
                  /* {console.log("Business_name",item.business_details[0]['name'])} */
                  /* <View
                        style={{ */
                  /* //   borderRadius: 10,
                          //   backgroundColor: "white",
                          //   overflow: "hidden",

                          // flexDirection: "column",
                          //   justifyContent: "flex-start",
                          //   alignSelf: "center",

                          //   marginTop: 10,
                          //   shadowColor: "#000",
                          //   shadowOffset: { width: 0, height: 2 },
                          //   shadowOpacity: 0.25,
                          //   shadowRadius: 3.84,
                          //   elevation: 5,
                        }}
                      > */
                  /* <View style={{flexDirection: "column"}}> */
                  /* <View style={{ flexDirection: "row" }}>
                          <View
                            style={{
                              padding: 10,
                              width: "100%",
                              // alignSelf: "center",
                              // alignItems: "center",
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
                              {item.delivery_person_name}
                            </Text> */

                  /* <View
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
                                {item.shipment_address}
                              </Text>
                            </View> */

                  /* </View> */
                  /* <View
                    style={{
                      width: "80%",
                      flexDirection: "row",
                      alignItems: "center",
                      justifyContent: "center",
                      marginTop: -5,
                    }}
                  >

                  </View> */
                  /* </View>
                          <View style={{ alignSelf: "center" }}>
                            <Text
                              style={{
                                marginBottom: 3,
                                fontSize: 14,
                                alignSelf: "flex-end",
                                marginRight: 10,
                                fontWeight: "bold",
                              }}
                            >
                              {item.no_of_items} items
                            </Text> */
                  /* <Text style={{ fontSize:12,alignSelf:'flex-end', color: "white",backgroundColor:Colors.darkRedColor,borderRadius:10,padding:5,}}>
                        {item.status}
                    </Text> */
                  /* </View>
                        </View>
                      </View> */

                  /* <Card>
            <CardItem>
              <Left>
              <Text style = {{color:'#0f70b7',fontSize:19,fontWeight:'bold'}}>{item.carrier_company}</Text>

               </Left>
                <Body>

                </Body>

              <Right><Text style =  {{fontSize:12,fontWeight:'bold'}}>Rs:{item.grand_total}/-</Text></Right>
            </CardItem>




            <CardItem style = {{borderTopWidth:1,borderTopColor:'lightgray'}}>
              <Left>
              <Text style = {{color:'gray'}}>{item.Origin_city}</Text>

              </Left>
              <Body>


              <Image
        style={{height:15,width:150,alignSelf:'center'}}
        source={require('../../assets/route.png')}
      />


              </Body>
              <Right>
              <Text style = {{color:'gray'}}>{item.Destination_city}</Text>

              </Right>
            </CardItem>

            {/* <CardItem>
              <Left>
              <Text style = {{color:'gray'}}>{item.Origin_city}</Text>
              </Left>
              <Body>




              </Body>
              <Right>
              <Text style = {{color:'gray'}}>{item.Destination_city}</Text>
              </Right>
            </CardItem> */

                  /* </Card>   */
                  /* </TouchableOpacity>
                  </Card> */
                )}
              />
            )}
          </View>
        </Content>
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
export default PendingOrders;
