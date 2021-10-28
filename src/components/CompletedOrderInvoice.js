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
// import * as DeliveryNoteAction from '../store/actions/DeliveryNote';
import * as ApiDataAction from "../store/actions/ApiData";
//import ViewShot from "react-native-view-shot";
import Colors from "../ColorCodes/Colors";
import URL from "../api/ApiURL";
import * as cartActions from "../store/actions/OrderBox";
import { useSelector, useDispatch } from "react-redux";
import MyHeader from "../components/MyHeader";
import InvoiceItem from "../components/InvoiceItem";
function CompletedOrderInvoice({ navigation, route }) {
  const dispatch = useDispatch();
  const clientImage = useSelector((state) => state.ApiData.ClientImage);
  const ClientId = useSelector((state) => state.ApiData.ClientId);
  const [isLoading, setIsLoading] = useState(false);
  const { OID, orderBoxId } = route.params;
  // const packages=Packages;
  const [invoiceData, setInvoiceData] = useState("");
  const [buttonLoading,setButtonLoading]=useState(false);
  const [orderBoxIdd,setOrderBoxIdd]=useState("");
  const [invoiceNo, setInvoiceNo] = useState("");
  const [orderList, setOrderList] = useState("");
  const [order, setOrder] = useState("");
  const [totalAmount, setTotalAmount] = useState("");
  const [RiderImage,setRiderImage]=useState("");
  const toggleBottomNavigationView = () => {
    //Toggling the visibility state of the bottom sheet
    setVisible(!visible);
  };
  // const OId=OrderId;
  // const OrderBoxId=OrderBox;
  // const totalQuantity=Quantity;
  // const id=OID;
  const orderId = OID;
  const d_orderBoxId = orderBoxId;
  // const SubQuantity=totalQuantity;
  // const dataDetails=dataDetail;

  const setting = () => {
    toggleBottomNavigationView();

    // if(dataStatus=="in_progress")
    // {

    // }
  };

  const sendInvoice = () => {
    fetch(URL+"/payment/create_list_invoice/",
      {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          inv_number: invoiceNo,
          total_amount: invoiceData.total_amount,
          order: invoiceData.id,
        }),
      }
    )
      .then(async (response) => {
        let data = await response.json();
        console.log("put", data);
        console.log("put", response.status);
        if (response.status == 201) {
          // dispatch(DeliveryNoteAction.AllClear(1)),
          console.log("Its work");
          alert("Your detail was submitted");
          navigation.navigate("Dashboard");

          // setCount(0);
          // navigation.navigate("Dashboard")
        }

        //send_Verification_Code()
        // navigation.navigate("VerificationCode" , {Email : email , Phone_No : phoneNumber})
      })
      .catch((error) => console.log("Something went wrong", error));
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
                  console.log("OrderrrrrrrIdddddddddddd: ",d_orderBoxId);
                  fetch(URL + "/order/list_order/" + d_orderBoxId + "/")
              // fetch(URL+'/client_app/clients_list/33/')
              .then((response) => response.json())
              .then((responseJson) => {
                console.log("OrderBoxDetail:", responseJson.order);
                // setBoxData(responseJson.order);

                dispatch(
                  cartActions.reorder(responseJson.order.order_products)
                )
                navigation.navigate("ReOrder", {
                  OID: orderId,
                  orderBoxId: d_orderBoxId,
                  Quantity: invoiceData.total_qty,
                  id:invoiceData.delivery_person_id,
                  name:invoiceData.delivery_person_name,
                  address:invoiceData.delivery_person_address
                })
                setButtonLoading(false);
                // setIsLoading(false);
                // setDataStatus(responseJson.order.status);
                // console.log(boxDetail, "-------");
                // setIsLoading(false);
              })
              .catch((error) => console.error(error));
                  // navigation.navigate("ReOrder", {
                  //   OID: orderId,
                  //   orderBoxId: d_orderBoxId,
                  //   Quantity: invoiceData.total_qty,
                  //   id:invoiceData.delivery_person_id,
                  //   name:invoiceData.delivery_person_name,
                  //   address:invoiceData.delivery_person_address
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
          console.log("OrderrrrrrrIdddddddddddd: ",d_orderBoxId);
          fetch(URL + "/order/list_order/" + d_orderBoxId + "/")
              // fetch(URL+'/client_app/clients_list/33/')
              .then((response) => response.json())
              .then((responseJson) => {
                console.log("OrderBoxDetail:", responseJson.order);
                // setBoxData(responseJson.order);

                dispatch(
                  cartActions.reorder(responseJson.order.order_products)
                )
                navigation.navigate("ReOrder", {
                  OID: orderId,
                  orderBoxId: d_orderBoxId,
                  Quantity: invoiceData.total_qty,
                  id:invoiceData.delivery_person_id,
                  name:invoiceData.delivery_person_name,
                  address:invoiceData.delivery_person_address
                })
                setButtonLoading(false);
                // setIsLoading(false);
                // setDataStatus(responseJson.order.status);
                // console.log(boxDetail, "-------");
                // setIsLoading(false);
              })
              .catch((error) => console.error(error));

        }




      }








  const getClientImage=(id)=>{
    fetch(URL + "/delivery_person/get_delivery_person_logo/"+id+"/")
            // fetch(URL+'/client_app/clients_list/33/')
            .then((response) => response.json())
            .then((responseJson) => {
              console.log(
                " Getting Image of client:",
                responseJson
              );
              setRiderImage(responseJson.image);
        setIsLoading(false);

            })
            .catch((error) => console.error(error));
}



  useEffect(() => {
    // getToken();

    // console.log("hi---------------")
    // console.log(PoNumber,"-----");
    console.log(orderId, "yoyo------");
    setIsLoading(true);
    console.log("From Invoice OrderBoxid", d_orderBoxId);
    console.log("From Invoice Orderid", orderId);

    if (orderId != "") {
      fetch(URL + "/payment/view_invoice/" + orderId + "/")
        // fetch(URL+'/client_app/clients_list/33/')
        .then((response) => response.json())
        .then((responseJson) => {
          console.log("Show Invoic", responseJson.order.order_products);
          setInvoiceNo(responseJson.order.inv_number);
          setOrderList(responseJson.order.order_products);
          setInvoiceData(responseJson.order);
          setTotalAmount(responseJson.order.total_amount);
          getClientImage(responseJson.order.delivery_person_id);

          // setIsLoading(false);
        })
        .catch((error) => console.error(error));
    }

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


  }, [orderId]);
  // console.log("Order Box Id:",OrderBoxId);
  // console.log("Order Box Id:",boxDetail);
  return (
    <View style={{ flex: 1 }}>
      {/* <MyHeader name="INVOICE" nav={navigation} /> */}
      <ScrollView>
        {isLoading ? (
          <Spinner color={Colors.themeColor} />
        ) : (
          <Content>
            <View style={styles.footer}>
              <View
                style={{
                  marginTop: 5,
                  elevation: 0,
                  shadowRadius: 0,
                  backgroundColor: "white",
                }}
              >
                <Text
                  style={{
                    alignSelf: "center",
                    flexDirection: "row",
                    fontSize: 16,
                    fontWeight: "bold",
                  }}
                >
                  {invoiceNo}
                </Text>
              </View>
              <View style={{flexDirection:'row',alignSelf:'center',padding:15,paddingTop:0,paddingBottom:0}}>

<Card style={{padding:10,width:'50%',backgroundColor:'#e6e6e6',elevation:0,borderRadius:7}}>
       {/* <View style={{flexDirection:'row'}}> */}
       <View style={{flexDirection:'row',alignSelf:'center',alignItems:'center',justifyContent:'center',width:"100%"}}>

<View style={{marginLeft:Platform.OS=="android"?0:0,width:"35%"}}>

 <Image source={RiderImage==null||RiderImage==""?require('../assets/profilelogo.png'):{uri:RiderImage}}
 style={{ width:Platform.OS=='ios'? 50:50,height:Platform.OS=='ios'? 50:50,borderRadius:60}}
 />

</View>

<View style={{paddingLeft:Platform.OS=="android"?5:0,width:"65%"}}>

 <Text style={{color:Colors.themeColor,fontSize:12}}>Delivery Person:</Text>



 <Text style={{fontSize:14,fontWeight:'bold'}}>{invoiceData.delivery_person_name}</Text>
 <Text style={{fontSize:12,color:'#666666'}}>{invoiceData.delivery_person_address}</Text>





</View>
</View>










</Card>

<Card style={{padding:10,marginLeft:10,width:'50%',backgroundColor:'#e6e6e6',elevation:0,borderRadius:7}}>
<View style={{flexDirection:'row',alignSelf:'center',alignItems:'center',justifyContent:'center',width:"100%"}}>

<View style={{marginLeft:Platform.OS=="android"?0:0,width:"35%"}}>

<Image source={clientImage==null||clientImage==""?require('../assets/profilelogo.png'):{uri:clientImage}}
style={{ width:Platform.OS=='ios'? 50:50,height:Platform.OS=='ios'? 50:50,borderRadius:60}}
/>

</View>

<View style={{paddingLeft:Platform.OS=="android"?5:0,width:"65%"}}>

<Text style={{color:Colors.themeColor,fontSize:12}}>Customer:</Text>



<Text style={{fontSize:14,fontWeight:'bold'}}>{invoiceData.client}</Text>
<Text style={{fontSize:12,color:'#666666'}}>{invoiceData.business_address}</Text>





</View>
</View>







       </Card>
       </View>

              <View
                style={{
                  elevation: 0,
                  shadowRadius: 0,
                  backgroundColor: "white",
                }}
              >
                <Text
                  style={{
                    alignSelf: "center",
                    flexDirection: "row",
                    fontSize: 16,
                    fontWeight: "bold",
                  }}
                >
                  {invoiceData.purchase_order_no}
                </Text>
              </View>
            </View>

            <View style={{flexDirection:'row',marginTop:30,}}>
        <Text style={{color:Colors.themeColor,width:"20%",fontSize:17,fontWeight:'bold',textAlign:"left"}}>Product</Text>
        {/* <Text style={{color:Colors.themeColor,width:35,fontSize:17,fontWeight:'bold',textAlign:'center'}}>Unit</Text> */}
        <Text style={{color:Colors.themeColor,width:"23%",fontSize:17,fontWeight:'bold',textAlign:'center'}}>Quantity</Text>
        <Text style={{color:Colors.themeColor,width:"20%",fontSize:17,fontWeight:'bold',textAlign:'center'}}>Unit Price</Text>

        <Text style={{color:Colors.themeColor,width:"16%",fontSize:17,fontWeight:'bold',textAlign:'center'}}>VAT</Text>

        <Text style={{color:Colors.themeColor,fontSize:17,fontWeight:'bold',width:"20%",textAlign:"right"}}>Amount</Text>
    </View>

            <View style={{ marginBottom: 10 }}>
              <FlatList
                data={orderList}
                keyExtractor={(item) => item.product_id}
                renderItem={(itemData) => (
                  <InvoiceItem
                    id={itemData.item.product_id}
                    quantity={itemData.item.purchased_qty}
                    total_amount={itemData.item.total_amount}
                    name={itemData.item.product_name}
                    unit={itemData.item.product_unit}
                    price={itemData.item.unit_sales_price}
                    vat={itemData.item.vat_amount}
                    amount={itemData.item.amount}
                  />
                )}
              />
              <View style={{flexDirection:'row',borderBottomWidth:0.5,borderBottomColor:'grey',marginTop:10}}>

<Text style={{color:Colors.themeColor,width:"22%",textAlign:'left',fontWeight:'bold',}}>Total</Text>
<Text style={{color:Colors.themeColor,width:Platform.OS=="android"?"20%":"20%",fontWeight:'bold',fontSize:14,textAlign:"center"}}>{invoiceData.total_qty}</Text>
{invoiceData.total_vat==0?<Text style={{color:Colors.themeColor,width:"33%",fontWeight:'bold',textAlign:"right",fontSize:14,}}>£ {invoiceData.total_vat}</Text>:<Text style={{color:Colors.themeColor,width:"33%",fontWeight:'bold',textAlign:"right",fontSize:14,}}>£ {parseFloat(invoiceData.total_vat).toFixed(2)}</Text>}

<Text style={{color:Colors.themeColor,width:"24%",fontWeight:'bold',textAlign:"right",fontSize:14}}>£ {parseFloat(invoiceData.total_amount).toFixed(2)}</Text>

</View>

            </View>

            <View style={{ padding: 10 }}></View>

            {invoiceData.delivery_note == "" ? null : (
              <View
                style={{
                  padding: 10,
                  paddingBottom: 0,
                  paddingTop: 0,
                  justifyContent: "center",
                }}
              >
                <Card
                  style={{
                    padding: 5,
                    elevation: 0,
                    backgroundColor: "#e6e6e6",
                    borderRadius: 7,
                  }}
                >
                  <Text style={{ textAlign: "center", width: "100%" }}>
                    {invoiceData.delivery_note}
                  </Text>
                </Card>
              </View>
            )}
            <View
              style={{
                flexDirection: "row",
                width: "100%",
                alignSelf: "center",
                padding: 10,
                paddingBottom: 0,
                justifyContent: "center",
              }}
            >



            {/* <View
                style={{
                  height: 100,
                  width: 100,
                  borderRadius: 120,
                  borderColor: Colors.textGreyColor,
                  borderWidth: 5,
                  marginTop: "3%",

                  marginBottom: 10,
                }}
              >
                <Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,
                    marginTop: "35%",
                    fontWeight: "bold",
                    fontSize: 12,
                    margin:'2%'
                  }}
                >
                  {invoiceData.order_delivery_datetime}
                </Text>
              </View> */}


{/* //=================== NEW UPDATION=======================// */}

{/* <View
                style={{

                  height: 110,
                 width: 110,
                  borderRadius: 120,
                  borderColor: Colors.textGreyColor,
                  borderWidth: 5,
                  marginTop: "3%",

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

                  {invoiceData?.order_delivery_datetime?.split(" ")[0]}

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
                  {invoiceData?.order_delivery_datetime?.split(" ")[1]}
                </Text>
              </View> */}


{/*  ------------------------------  ---------------------------- */}
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
                  {invoiceData?.order_delivery_datetime?.split(" ")[0]}
                </Text>

                <Text
                  style={{
                    textAlign: "center",
                    color: Colors.themeColor,
                    fontSize: 12,
                  }}
                >
                  {invoiceData?.order_delivery_datetime?.split(" ")[1]}
                </Text>


              </View>





              <View style={{ alignSelf: "center", marginLeft: "5%" }}>
                <Text style={{ color: Colors.productGrey, fontSize: 14 }}>
                  Delivery Address:{" "}
                </Text>
                <Text style={{ fontSize: 16, width: 210 }}>
                  {invoiceData.business_address}
                </Text>
              </View>
            </View>
            <View style={{alignSelf:'center'}}>
            <TouchableOpacity onPress={reorder} style={styles.button}>
            {buttonLoading ? (
                <Spinner color={"white"} />
              ) : (
            <Text style={styles.buttonText}>Reorder</Text>)}
            </TouchableOpacity>
        </View>
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
    // backgroundColor:'#FFF',
    // alignItems: 'center',
    // justifyContent: 'center',
    // alignSelf:"center",
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
    // paddingTop: 30,
    //backgroundColor: '#ecf0f1',
    //padding: 8,
  },
  note_inputArea: {
    alignSelf: "center",
    marginVertical: 10,
    height: 60,
    width: "100%",
    backgroundColor: "#E6E6E6",
    borderRadius: 10,
    paddingHorizontal: 30,
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
    // borderTopLeftRadius: 30,
    // borderTopRightRadius: 30,
    //paddingVertical: 10,
    // paddingHorizontal: 60,
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
    borderRadius: 25,
    marginVertical: 20,
  },
  s_button: {
    height: 40,
    width: 300,
    backgroundColor: Colors.themeColor,
    justifyContent: "center",
    borderRadius: 25,
    // marginVertical: 5,
  },

  buttonText: {
    fontSize: 20,
    color: "#ffffff",
    fontWeight: "800",
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

export default CompletedOrderInvoice;
