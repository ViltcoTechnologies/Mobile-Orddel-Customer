import React, { Component } from "react";
import { useState, useEffect } from "react";
import {
  Image,
  ScrollView,
  ActivityIndicator,
  FlatList,
  TouchableHighlight,
  TouchableOpacity,
} from "react-native";
import {
  Container,
  Header,
  Spinner,
  Card,
  CardItem,
  Title,
  Thumbnail,
  Text,
  Button,
  Left,
  Body,
  Right,
  View,
} from "native-base";
import Colors from '../../ColorCodes/Colors';
//import ViewShot from "react-native-view-shot";
import Ionicons from 'react-native-vector-icons/Ionicons';
import FontAwesome from 'react-native-vector-icons/FontAwesome';
import URL from "../../api/ApiURL";
import MyHeader from '../../components/MyHeader';

const ShippmentAddresses = ({ navigation, route }) => {
//   const { Shipper_ID } = route.params;
  const [isLoading, setIsLoading] = useState(true);
  const [data, setData] = useState([]);
  const [list, setList] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
      console.log("hi---------------")
    //fetch(URL+"/client_app/list_business/")
    // fetch(URL+'/client_app/clients_list/33/')
    fetch(URL+"/client_app/clients_list/33/")
    .then((response) => response.json())
.then((responseData) => {
          console.log("Buisness Detail:",responseData);
        // if (json["response"] == "Record does not exist or not found") {
        //   setLoading(true);
        // } else {
        //   setData(json);
        //   //console.log(json);
        // }
      })
      .catch((error) => console.error(error))
      .finally(() => setIsLoading(false));

    //console.log(data)
  }, []);
  function currencyFormat(num) {
    return "Rs " + num.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
  }

  return (
    <View style={{ flex: 1,height:'100%' }}>
      <MyHeader name="ADDRESSES" nav={navigation}/>

      {loading && (
        <View
          style={{
            justifyContent: "center",
            alignItems: "center",
            marginTop: "30%",
          }}
        >
          <FontAwesome name="exclamation-circle" color={Colors.themeColor} size={150} />
          <Text style={{ color: Colors.themeColor, fontWeight: "bold",marginTop:20, fontSize: 25 }}>
            NO RECORD
          </Text>
        </View>
      )}
      {isLoading ? (
        <Spinner color="#0f70b7" />
      ) : (
        <FlatList
          data={data}
          showsVerticalScrollIndicator={false}
          keyExtractor={({ id }, index) => id}
          renderItem={({ item }) => (
            <TouchableOpacity
              // onPress = {() => navigation.navigate("PendingDetails" , {Due_Date : item.due_date , Invoice_Total : item.grand_total,Carrier_Name : item.carrier_company ,Load_Type : item.load_type,Origin_City : item.Origin_city,Destination_City : item.Destination_city,Delivery_Option : item.Delivery_Option,Cargo_Amount : item.Cargo_amount,Cargo_Type : item.Cargo_Type,Cargo_Product_Type : item.Cargo_Product_type,Cargo_Product_List : item.Cargo_Product_List,Booking_Status : item.booking_status})}
              onPress={() =>
                navigation.navigate("PaymentHistoryDetail")
              }
            >
              <View
                style={{
                  borderRadius: 10,
                  backgroundColor: "white",
                  overflow: "hidden",
                  flexDirection: "column",
                  justifyContent: "flex-start",
                  alignSelf: "center",
                  width: "95%",
                  marginTop: 10,
                  shadowColor: "#000",
                  shadowOffset: { width: 0, height: 2 },
                  shadowOpacity: 0.25,
                  shadowRadius: 3.84,
                  elevation: 5,
                }}
              >
                <View
                  style={{
                    marginTop: 10,
                    padding: 10,
                    width: "100%",
                    alignSelf: "center",
                    alignItems: "center",
                    justifyContent: "flex-start",
                    borderBottomColor: "#b3b3b3",
                    borderBottomWidth: 0.5,
                  }}
                >
                  <View
                    style={{
                      width: "100%",
                      flexDirection: "row",
                      justifyContent: "flex-end",
                      marginTop: "1%",
                    }}
                  ></View>
                  <View
                    style={{
                      flexDirection: "row",
                      alignItems: "center",
                      justifyContent: "space-between",
                      width: "100%",
                    }}
                  >
                    <View>
                      <Text
                        style={{
                          marginLeft: "3%",
                          color: "#0f70b7",
                          fontSize: 15,
                          fontWeight: "bold",
                        }}
                      >
                        {item.business_name}
                      </Text>
                    </View>
                    {/* <View>
                      <Text
                        style={{
                          marginRight: "3%",
                          fontSize: 15,
                          fontWeight: "bold",
                          color: "gray",
                        }}
                      >
                        {currencyFormat(item.grand_total)}\-
                      </Text>
                      <Text note>{item.invoice_no}</Text>
                    </View> */}
                  </View>
                  {/* <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'flex-end', width: '100%' }}>
                                <Text style={{ marginRight: '3%', color: "#0f70b7", fontSize: 15, fontWeight: 'bold' }}>{item.booking_status}</Text>
                            </View> */}
                </View>
                <View
                  style={{
                    padding: 10,
                    width: "100%",
                    alignSelf: "center",
                    alignItems: "center",
                    justifyContent: "flex-start",
                  }}
                >
                  <Text
                    style={{
                      fontSize: 15,
                      fontWeight: "bold",
                      marginTop: "4%",
                    }}
                  >
                    Route
                  </Text>
                  <View
                    style={{
                      width: "80%",
                      flexDirection: "row",
                      alignItems: "center",
                      justifyContent: "center",
                      marginTop: -5,
                    }}
                  >
                    <View
                      style={{
                        height: 15,
                        width: 15,
                        borderRadius: 50,
                        backgroundColor: "#0f70b7",
                      }}
                    ></View>
                    <View
                      style={{
                        width: "80%",
                        height: 4,
                        backgroundColor: "#0f70b7",
                      }}
                    ></View>
                    <View
                      style={{
                        height: 15,
                        width: 15,
                        borderRadius: 50,
                        backgroundColor: "#0f70b7",
                      }}
                    ></View>
                  </View>
                  <View
                    style={{
                      width: "75%",
                      flexDirection: "row",
                      alignItems: "center",
                      justifyContent: "space-between",
                      marginTop: "1.5%",
                    }}
                  >
                    <Text style={{ fontSize: 15, color: "grey" }}>
                      {item.business_nature}
                    </Text>
                    <Text style={{ fontSize: 15, color: "grey" }}>
                      {item.business_type}
                    </Text>
                  </View>
                </View>
              </View>

              {/* <Card>
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
            </CardItem> */}

               {/* </Card>   */}
            </TouchableOpacity>
          )}
        />
      )}
    </View>
  );
};
export default ShippmentAddresses;