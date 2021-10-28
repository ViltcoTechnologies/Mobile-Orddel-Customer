import React, { useState, useEffect } from "react";
import {
  Image,
  ScrollView,
  ActivityIndicator,
  FlatList,
  TouchableHighlight,
  TouchableOpacity,
  StyleSheet,
  LogBox,
  TextInput,
} from "react-native";

import {
  Container,
  Header,
  Spinner,
  Card,
  CardItem,
  Title,
  Thumbnail,
  Item,
  Content,
  Text,
  Button,
  Left,
  Body,
  Right,
  View,
} from "native-base";
import { Picker } from "@react-native-picker/picker";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import AntDesign from "react-native-vector-icons/AntDesign";

//import ViewShot from "react-native-view-shot";
import Colors from "../ColorCodes/Colors";
import Ionicons from "react-native-vector-icons/Ionicons";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import URL from "../api/ApiURL";
import { useSelector, useDispatch } from "react-redux";
import * as cartActions from "../store/actions/OrderBox";
import * as ApiAction from "../store/actions/ApiData";
import MyHeader from "../components/MyHeader";
import ReorderCartItem from "../components/ReorderCartItem";
import * as ApiDataAction from "../store/actions/ApiData";
import { BottomSheet } from "react-native-btr";
import { Platform } from "react-native";

function OrdersStatus({ navigation, route }) {
  const dispatch=useDispatch();
  const { OrderBox, OrderId, Packages, Quantity } = route.params;
  const packages = Packages;
  const [boxData, setBoxData] = useState("");
  const ClientImage = useSelector((state) => state.ApiData.ClientImage);
  const ClientId = useSelector((state) => state.ApiData.ClientId);
  const [boxDetail, setBoxDetail] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [status, setStatus] = useState("");
  const [dataStatus, setDataStatus] = useState("");
  const [note, setNote] = useState("");
  const [disvisible, setDisvisible] = useState(false);
  const [visible, setVisible] = useState(false);
  const [orderBoxId,setOrderBoxId]=useState("");
  const [buttonLoading,setButtonLoading]=useState(false);
  const [orderBoxIdd,setOrderBoxIdd]=useState("");
  const toggleBottomNavigationView = () => {
    //Toggling the visibility state of the bottom sheet
    setVisible(!visible);
  };
  const OId = OrderId;
  const OrderBoxId = OrderBox;
  const totalQuantity = Quantity;
 const actualTime = boxData.order_delivery_datetime
//  const wakt= actualTime.split('')[0];
//  const tarik= actualTime.split('')[1];


 console.log(actualTime,' --------- time-----------');


  const setting = () => {
    toggleBottomNavigationView();

    // if(dataStatus=="in_progress")
    // {

    // }
  };




  const reorder=()=>{
setButtonLoading(true);
    if(orderBoxIdd==""){
      fetch(URL + "/order/create_order_box/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          client_id: ClientId,
        }),
      })
        .then(async (response) => {
          let data = await response.json();

          console.log(response)
          console.log("Create",data )
          // console.log("status code",response.status)
          // console.log("status data",data)
          // setStatusCode(response.status)
          if (response.status == 201) {
              // setResMessage("")

              dispatch(ApiDataAction.SetOrderBoxId(data.cart.id));
              fetch(URL + "/order/list_order/" + OrderBoxId + "/")
              // fetch(URL+'/client_app/clients_list/33/')
              .then((response) => response.json())
              .then((responseJson) => {
                console.log("OrderBoxDetail:", responseJson.order);
                // setBoxData(responseJson.order);

                dispatch(
                  cartActions.resend(responseJson.order.order_products)
                )
                navigation.navigate("ReOrder", {
                  OID: OId,
                  orderBoxId: OrderBoxId,
                  Quantity: totalQuantity,
                  id:boxData.delivery_person,
                  name:boxData.delivery_person_name,
                  address:boxData.delivery_person_address
                })
                setButtonLoading(false);
                // setIsLoading(false);
                // setDataStatus(responseJson.order.status);
                // console.log(boxDetail, "-------");
                // setIsLoading(false);
              })
              .catch((error) => console.error(error));
              // navigation.navigate("ReOrder", {
              //   OID: OId,
              //   orderBoxId: OrderBoxId,
              //   Quantity: totalQuantity,
              //   id:boxData.delivery_person,
              //   name:boxData.delivery_person_name,
              //   address:"142-Allama Iqbal Road"
              // })
              // setButtonLoading(false);

          } else {
            console.log("execption: ",data.message);
            alert(data.message);
            setButtonLoading(false);
            // Toast.show(data.message, Toast.LONG);
            // setResMessage(data.message)

          }


          // code that can access both here
        })
        .catch((error) => console.log("Something went wrong", error));
    }
    else{
      fetch(URL + "/order/list_order/" + OrderBoxId + "/")
              // fetch(URL+'/client_app/clients_list/33/')
              .then((response) => response.json())
              .then((responseJson) => {
                console.log("OrderBoxDetail:", responseJson.order);
                // setBoxData(responseJson.order);

                dispatch(
                  cartActions.resend(responseJson.order.order_products)
                )
                navigation.navigate("ReOrder", {
                  OID: OId,
                  orderBoxId: OrderBoxId,
                  Quantity: totalQuantity,
                  id:boxData.delivery_person,
                  name:boxData.delivery_person_name,
                  address:boxData.delivery_person_address
                })
                setButtonLoading(false);
                // setIsLoading(false);
                // setDataStatus(responseJson.order.status);
                // console.log(boxDetail, "-------");
                // setIsLoading(false);
              })
              .catch((error) => console.error(error));
      // navigation.navigate("ReOrder", {
      //   OID: OId,
      //   orderBoxId: OrderBoxId,
      //   Quantity: totalQuantity,
      //   id:boxData.delivery_person,
      //   name:boxData.delivery_person_name,
      //   address:boxData.delivery_person_address
      // })
      // setButtonLoading(false);
    }




  }




  const accept = () => {
    setIsLoading(true);
    fetch(URL + "/delivery_person/update_order_status/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        order_id: OId,
        delivery_person_action: "accepted",
      }),
    })
      .then(async (response) => {
        let data = await response.json();

        //    console.log("signup",response.status)
        if (response.status == 200) {
          setIsLoading(false);
          navigation.navigate("Dashboard");
        } else {
          alert(data.detail);
        }
        //send_Verification_Code()
        // navigation.navigate("VerificationCode" , {Email : email , Phone_No : phoneNumber})
      })
      .catch((error) => console.log("Something went wrong", error));
    // toggleBottomNavigationView();
    setDisvisible(true);
  };
  const purchase = () => {
    setIsLoading(true);
    fetch(URL + "/delivery_person/update_order_status/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        order_id: OId,
        delivery_person_action: "purchased",
      }),
    })
      .then(async (response) => {
        let data = await response.json();

        //    console.log("signup",response.status)
        if (response.status == 200) {
          setIsLoading(false);
          navigation.navigate("Dashboard");
        } else {
          alert(data.detail);
        }
        //send_Verification_Code()
        // navigation.navigate("VerificationCode" , {Email : email , Phone_No : phoneNumber})
      })
      .catch((error) => console.log("Something went wrong", error));

    // toggleBottomNavigationView();
    setDisvisible(true);
  };

  useEffect(() => {
    // getToken();
    //   console.log("hi---------------")
    // console.log(PoNumber,"-----");
    // console.log(OrderId,"------")
    if(ClientId!=0){
      fetch(URL + "/order/get_order_box/" + ClientId + "/")
      // fetch(URL+'/client_app/clients_list/33/')
      .then((response) => response.json())
      .then((responseJson) => {
        // console.log(
        //   "Dashboard:",
        //   responseJson
        // );
        console.log("OrderBoxId:", responseJson);
        setOrderBoxIdd(responseJson.order_box);
        if(responseJson.order_box!=""){
          dispatch(ApiDataAction.SetOrderBoxId(responseJson.order_box));

        }

      })
      .catch((error) => console.error(error));
    }




    setIsLoading(true);
    fetch(URL + "/order/list_order/" + OrderBoxId + "/")
      // fetch(URL+'/client_app/clients_list/33/')
      .then((response) => response.json())
      .then((responseJson) => {
        console.log("OrderBoxDetail:", responseJson.order);
        setBoxData(responseJson.order);
        setBoxDetail(responseJson.order.order_products);
        setIsLoading(false);
        setDataStatus(responseJson.order.status);
        console.log(boxDetail, "-------");
        setIsLoading(false);

      })
      .catch((error) => console.error(error));
    setDisvisible(false);
    // .finally(() => setIsLoading(false));

    //console.log(data)
  }, [OrderBoxId, disvisible]);
  // console.log("Order Box Id:",OrderBoxId);
  // console.log("Order Box Id:",boxDetail);
  return (
    <View style={{ flex: 1 }}>
      {/* <MyHeader name="ORDERS STATUS" nav={navigation} /> */}

      <ScrollView>
        {isLoading ? (
          <Spinner color={Colors.themeColor} />
        ) : (
          <Content>
            <View style={styles.footer}>
              <View
                style={{
                  flexDirection: "row",
                  marginBottom: "5%",
                  alignItems: "center",
                }}
              >
                <View
                  style={{
                    paddingTop: Platform.OS == "ios" ? '5%' : '5%',
                    paddingLeft: '2%',
                  }}
                >
                  <Image
                    source={
                      ClientImage == ""||ClientImage==null
                        ? require("../assets/profilelogo.png")
                        : { uri: ClientImage }
                    }
                    style={{
                      width: Platform.OS == "ios" ? 130 : 80,
                      height: Platform.OS == "ios" ? 130 : 80,
                      borderRadius:60
                    }}
                  />
                </View>

                <View
                  style={{
                    paddingTop: Platform.OS == "ios" ? 0 : 0,
                    paddingLeft: '4%',
                    alignSelf: "center",
                  }}
                >
                  <Text
                    style={{
                      color: "black",
                      fontWeight: "bold",
                      borderBottomWidth: 2,
                      borderBottomColor: Colors.textGreyColor,
                      fontSize: Platform.OS == "android" ? 20 : 20,
                      alignSelf: "flex-start",
                      width: 230,
                    }}
                  >
                    {boxData.client}
                  </Text>
                  <Text style={{fontSize: 13, fontWeight:'600' }}>Order No: </Text>
                  <Text style={{fontSize: 13, marginTop: 2 , marginRight:'3%',
                  width:Platform.OS=="android"? '80%':'80%',
                alignSelf: "flex-start",
                }}>
                     {boxData.purchase_order_no}
                     {/* fghvcsdfjsbfdsjfbdfnfbjhsbfjsfbksjdbfksdjbfjsdkfbkjdsfbkjsfbsdfbjsdbfjdsbfksfnjksnjfkdsn */}
                     {/* 12323344455555557756544534535646758687696756456233434343434343 */}
                  </Text>
                </View>
              </View>
            </View>
            <View
              style={{
                flexDirection: "row",
                borderBottomColor: Colors.textGreyColor,
                borderBottomWidth: 1,
                width: "90%",
                alignSelf: "center",
              }}
            >

              {/* <View
                style={{
                  // height: 100,
                  // width: '30%',
                  height: 110,
                 width: 110,
                  borderRadius: 120,
                  borderColor: Colors.textGreyColor,
                  borderWidth: 5,
                  marginTop: "3%",
                  //borderWidth:5,
                  marginBottom: 10,
                }}
              >

<Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,
                    marginTop: "20%",
                    fontWeight: "bold",
                    fontSize: 12,
                    margin:'2%'
                  }}
                >
                    Date & Time

                </Text>
                <Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,

                    fontWeight: "bold",
                    fontSize: 12,
                    margin:'2%'
                  }}
                >

                  {boxData?.order_delivery_datetime?.split(" ")[0]}

                </Text>
                <Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,
                    //marginTop: "35%",
                    fontWeight: "bold",
                    fontSize: 12,
                    margin:'2%'
                  }}
                >

                  {boxData?.order_delivery_datetime?.split(" ")[1]}
                </Text>
              </View> */}




              <View
                style={{
                  height: 100,
                  width: 100,
                  borderRadius: 100,
                  borderColor: Colors.textGreyColor,
                  borderWidth: 5,
                  marginTop: "3%",
                  marginBottom: 12,
                }}
              >
                <Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,
                    marginTop: "12%",
                    fontWeight: "bold",
                    fontSize: 12,
                    margin:'2%',

                  }}
                >

                Delivery

                </Text>
                <Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,
                    //marginTop: "20%",
                    fontWeight: "bold",
                    fontSize: 12,
                    margin:'2%',

                  }}
                >
                Date & Time

                </Text>
                <Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,
                    //marginTop: "35%",
                    //fontWeight: "bold",
                    fontSize: Platform.OS == "android" ? 12 : 11,
                  }}
                >
                  {boxData.order_delivery_datetime}
                </Text>
              </View>






              {/* -------------------------- */}

              <View style={{ alignSelf: "center", marginLeft: "5%" }}>
                <View
                  style={{
                    backgroundColor: Colors.themeColor,
                    height: 15,
                    borderRadius: 2,
                    width: "45%",
                  }}
                >
                  <Text
                    style={{
                      color: "white",
                      fontSize: 12,
                      fontWeight: "bold",
                      textAlign: "center",
                    }}
                  >
                    {dataStatus.toUpperCase()}
                  </Text>
                </View>
                <Text style={{ color: Colors.productGrey, fontSize: 14 }}>
                  Delivery Address:{" "}
                </Text>
                <Text style={{ fontSize: 16, width: 210 }}>
                  {boxData.business_address}
                </Text>
              </View>
            </View>

            <View style={{flexDirection:'row',marginTop:30,}}>
        <Text style={{color:Colors.themeColor,width:"30%",fontSize:17,fontWeight:'bold',textAlign:"left",marginLeft:"1%"}}>Product</Text>
        <Text style={{color:Colors.themeColor,width:"20%",fontSize:17,fontWeight:'bold',textAlign:'center'}}>Unit</Text>
        <Text style={{color:Colors.themeColor,width:"20%",fontSize:17,fontWeight:'bold',textAlign:'center'}}>Quantity</Text>
        <Text style={{color:Colors.themeColor,fontSize:17,fontWeight:'bold',marginRight:20,width:"25%",textAlign:"right"}}>Last month Avg.Price</Text>
    </View>

            <View
              style={{
                borderBottomColor: Colors.textGreyColor,
                borderBottomWidth: 2,
                marginBottom: 10,
              }}
            >
              <FlatList
                data={boxDetail}
                keyExtractor={(item) => item.product_id}
                renderItem={(itemData) => (
                  <ReorderCartItem
                    id={itemData.item.product_id}
                    quantity={itemData.item.quantity}
                    total_amount={itemData.item.total_amount}
                    name={itemData.item.product_name}
                    unit={itemData.item.product_unit}
                    price={itemData.item.avg_price}
                  />
                )}
              />
              <View
                style={{
                  flexDirection: "row",
                  width: "100%",
                  // borderBottomWidth: 0.5,
                  // borderBottomColor: "grey",
                  marginTop: 10,
                }}
              >
                <Text
                  style={{
                    color: Colors.themeColor,
                    width: "22.5%",
                    textAlign: "left",
                    marginLeft: "1%",
                    fontWeight:'bold'
                  }}
                >
                  Total
                </Text>
                <Text
                  style={{
                    color: Colors.themeColor,
                    width: "75%",
                    textAlign: "center",
                    // paddingLeft: "15%",
                    fontWeight:'bold'
                  }}
                >
                  {totalQuantity}
                </Text>


              </View>
              {/* <View style={{ flexDirection: "row" }}>
                <Text style={{ color: Colors.themeColor, marginLeft: "5%" }}>
                  Total Packages:
                </Text>
                <Text style={{ color: Colors.themeColor, marginLeft:Platform.OS=="android"? "20%":"24%" }}>
                  {totalQuantity}
                </Text>
              </View> */}


            </View>
            {boxData.status=="in progress"?
            <TouchableOpacity onPress={reorder} style={styles.button}>
              {buttonLoading ? (
                <Spinner color={"white"} />
              ) : (
            <Text style={styles.buttonText}>Reorder</Text>)}
            </TouchableOpacity>:null}
          </Content>
        )}


      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    // backgroundColor: '#EE0202',
  },
  activityIndicator: {
    fontSize: 25,
    width: "60%",
    color: Colors.accentColor,
  },

  spinner: {
    //flex: 1,
    position: "absolute",
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    justifyContent: "center",
    alignItems: "center",

  },

  signupContianer: {
    flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
  },
  signupText: {
    fontSize: 14,
    fontWeight: "bold",
    // color:'rgba(255,255,255, 0.7)',
    color: "black",
  },
  signupButton: {
    fontWeight: "bold",
    backgroundColor: "#EE0202",
    fontSize: 20,
    width: 100,
    height: 30,
    borderRadius: 25,
  },
  header: {
    flex: 1,
    width: "100%",
    //backgroundColor:'#EE0202',
    justifyContent: "center",
    alignItems: "center",
  },

  footer: {
    backgroundColor: "#ffffff",

  },
  g_container: {
    // flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  inputArea: {
    marginVertical: 15,
    height: 40,
    width: "100%",
    backgroundColor: "white",
    borderColor: Colors.textGreyColor,
    borderWidth: 2,

    borderRadius: 5,
    paddingHorizontal: 30,
  },
  button: {
    height: 40,
    width: 300,
    backgroundColor: Colors.themeColor,
    justifyContent: "center",
    alignSelf:'center',
    borderRadius: 25,
    marginVertical: 20,
  },
  s_button: {
    height: 40,
    width: 300,
    backgroundColor: Colors.themeColor,
    justifyContent: "center",
    borderRadius: 25,
    //   marginVertical: 5,
  },

  buttonText: {
    fontSize: 20,
    color: "#ffffff",
    fontWeight: "bold",
    textAlign: "center",
  },
  bottomNavigationView: {
    backgroundColor: "#fff",
    width: "100%",
    height: 90,
    // justifyContent: 'center',
    //alignItems: 'center',
  },
});

export default OrdersStatus;
