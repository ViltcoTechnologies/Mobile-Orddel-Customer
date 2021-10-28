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
import { useSelector, useDispatch } from "react-redux";
//import ViewShot from "react-native-view-shot";
import Colors from "../ColorCodes/Colors";
import Ionicons from "react-native-vector-icons/Ionicons";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import URL from "../api/ApiURL";

import * as cartActions from "../store/actions/OrderBox";
import MyHeader from "../components/MyHeader";
// import { useIsFocused } from "@react-navigation/native";
import { useIsFocused } from "@react-navigation/native";

// import * as ApiAction from "../store/actions/ApiData";

const RejectedOrders = ({ navigation, route }) => {
  const dispatch = useDispatch();
  //   const isFocused = useIsFocused();
  const {Id, name ,address} = route.params
  const RiderId=Id;
  const RiderName=name;
  const RiderAddress=address;
  const ClientId = useSelector((state) => state.ApiData.ClientId);
  console.log("ClientId", ClientId);
  //   const { Shipper_ID } = route.params;
  const isFocused = useIsFocused();

  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState([]);
  const [list, setList] = useState("");
  const [loading, setLoading] = useState(false);
  const [id, setId] = useState();

  const [orderBoxId, setOrderBoxId] = useState();
  const [handleIt, setHandleIt] = useState(false);
  const [loadingIt, setLoadingIt] = useState(false);


  const forward=()=>{
    console.log("OrderBoxId:",orderBoxId)
    // fetch(URL + "/order/list_order/" + orderBoxId + "/")
    //           // fetch(URL+'/client_app/clients_list/33/')
    //           .then((response) => response.json())
    //           .then((responseJson) => {
    //             console.log("OrderBoxDetail:", responseJson.order);
    //             // setBoxData(responseJson.order);

    //             dispatch(
    //               cartActions.resend(responseJson.order.order_products)
    //             )
    //             navigation.navigate("RejectedOrdersStatus", {
    //               OID: id,
    //               orderBoxId: orderBoxId,
    //               // Quantity: item.total_quantity,
    //               id:RiderId,
    //               name:RiderName,
    //               address:RiderAddress
    //             })
    //             // setButtonLoading(false);
    //             // setIsLoading(false);
    //             // setDataStatus(responseJson.order.status);
    //             // console.log(boxDetail, "-------");
    //             // setIsLoading(false);
    //           })
    //           .catch((error) => console.error(error));
  }


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
        "&choice=rejected"
    )
      // fetch(URL+'/client_app/clients_list/33/')
      .then(async (response) => {
        let data = await response.json();
        //console.log("status code", response.status);
        //console.log("status code-----------------", data.response[0].id);

        if (response.status == 200) {
          if (data.response == "") {
            setLoading(true);
            setIsLoading(false);
          } else {
            setId(data.response[0].id);
            setOrderBoxId(data.response[0].order_box);
            console.log("Rejected:", data);
            setLoading(false);
            setData(data);

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
                data={data.response}
                // inverted={true}
                style={{ alignSelf: "center" }}
                showsVerticalScrollIndicator={false}
                // keyExtractor={item => item.index_id.toString()}
                keyExtractor={({ id }, index) => id}
                renderItem={({ item }) => (

                  <TouchableOpacity
                    style={{ marginTop: 5, marginBottom: 5 }}
                    disabled={handleIt? true: false}
                    onPress={()=>{
                      setLoadingIt(true);
                      console.log("hello",item.order_box);
                      fetch(URL + "/order/list_order/" + item.order_box + "/")
              // fetch(URL+'/client_app/clients_list/33/')
              .then((response) => response.json())
              .then((responseJson) => {
                console.log("OrderBoxDetail:", responseJson.order);
                // setBoxData(responseJson.order);
                setLoadingIt(false)
                dispatch(
                  cartActions.resend(responseJson.order.order_products)
                )
                navigation.navigate("RejectedOrdersStatus", {
                  OID: item.id,
                  orderBoxId: item.order_box,
                  // Quantity: item.total_quantity,
                  id:RiderId,
                  name:RiderName,
                  address:RiderAddress
                })

              })
              .catch((error) => console.error(error));
                    }}


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
export default RejectedOrders;
