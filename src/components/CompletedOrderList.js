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
  Linking,
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

//import ViewShot from "react-native-view-shot";
import Colors from "../ColorCodes/Colors";
import Ionicons from "react-native-vector-icons/Ionicons";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import URL from "../api/ApiURL";
import { useSelector, useDispatch } from "react-redux";
import MyHeader from "../components/MyHeader";

import * as ApiAction from "../store/actions/ApiData";
const CompletedOrderList = ({ navigation, route }) => {
  const isFocused = useIsFocused();

  const ClientId = useSelector((state) => state.ApiData.ClientId);
  console.log("ClientId", ClientId);
  //   const { Shipper_ID } = route.params;
  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState([]);
  const [list, setList] = useState("");
  const [loading, setLoading] = useState(false);
  const [id, setId] = useState();

  const [orderBoxId, setOrderBoxId] = useState();
  const [invoiceId, setInvoiceId] = useState();
  useEffect(() => {
    if (invoiceId) sendInvoice()
  }, [invoiceId])

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
        "&choice=delivered"
    )
      // fetch(URL+'/client_app/clients_list/33/')
      .then(async (response) => {
        let data = await response.json();
        //console.log("status code", response.status);
        //console.log("Completed Order-----------------", data);

        if (response.status == 200) {
          if (data.response == "") {
            setLoading(true);
            setIsLoading(false);
          } else {
            setId(data.response[0].id);
            setOrderBoxId(data.response[0].order_box);
            //console.log("InProgress:", data);
            setLoading(false);
            setData(data);
            setIsLoading(false);
          }
        } else {
          setLoading(true);
          setIsLoading(false);
        }


      })
      .catch((error) => console.error(error))
      .finally(() => setIsLoading(false));

    console.log(data);
  }, [isFocused]);


  const sendInvoice = () => {

    console.log(invoiceId,'.... invoiceId  ....');
    if(invoiceId)
    {
      Linking.openURL(
        URL + "/payment/generate_invoice_pdf/" +invoiceId+ "/?download=true"
      );
      console.log("Its work");
      //navigation.navigate("Dashboard");
    }


  };


  const sequenceByDate = data?.response?.sort(function(a, b){

    // console.log(a.order_delivery_datetime,'========>> a date');
    // console.log(b.order_delivery_datetime,'========>> b date');
    // let first = parseInt(a.order_delivery_datetime, 10);
    let first = a.order_delivery_datetime.split(" ")[0];
    let second = b.order_delivery_datetime.split(" ")[0];


     console.log('date a =====>> ',first);
     console.log('date b =====>> ',second);


    if(a.first < b.second) { return -1; }
    if(a.first > b.second) { return 1; }
    return 0;
})

  //const sequenceByDate = data?.response?.slice().sort((a, b) => b.order_delivery_datetime - a.order_delivery_datetime);
  console.log("sequence by date:========>>>>> ",sequenceByDate);

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
                // data={data.response}
                data={sequenceByDate}

                style={{ alignSelf: "center" }}
                showsVerticalScrollIndicator={false}
                // keyExtractor={item => item.index_id.toString()}
                keyExtractor={({ id }, index) => id}
                renderItem={({ item }) => (
                  <TouchableOpacity
                    style={{ marginTop: 5, marginBottom: 5 ,  }}
                    onPress={() =>{
                      // console.log("OrderId",item.id);
                      // console.log("OrderBoxId",item.order_box)
                      navigation.navigate("CompletedOrderInvoice", {
                        OID: item.id,
                        orderBoxId: item.order_box,
                      })

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
                        // borderWidth:1
                      }}
                    >
                      <View
                        style={{
                          width: "50%",
                          justifyContent: "center",
                          paddingLeft: 23,
                          //borderWidth:1
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
                          width: "35%",
                          justifyContent: "center",
                          //alignItems: "flex-end",
                          paddingLeft: 23,
                          // borderWidth:1
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
                          {item.total_purchased_quantity} Packages
                        </Text>
                      </View>


                      <TouchableOpacity onPress={() =>
                        {
                          console.log("item.invoice_id =====>>>>",item)
                          if(item.id){
                            setInvoiceId(item.id)
                          }else{
                            alert("Invoice not created!")
                          }
                          // sendInvoice()

                        }

                      }
                          style={{
                          width: "15%",
                          justifyContent: "center",
                          alignItems: "center",
                          // paddingLeft: 23,
                          //  borderWidth:1
                          }}
                      >


                    <FontAwesome
                      name="download"
                      size={30}
                      // style={styles.iconStyle}
                      color={Colors.darkRedColor}
                      style={{ alignSelf: "center",   }}
                    />
                    </TouchableOpacity>

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
export default CompletedOrderList;
