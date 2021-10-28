import React, { useState, useEffect } from "react";
import {
  StyleSheet,
  View,
  ImageBackground,
  TouchableOpacity,
  Image,
  ScrollView,
  LogBox,
  FlatList,
  StatusBar,
  SafeAreaView,
  Animated,
  TextInput,
  Platform,
  BackHandler,
  KeyboardAvoidingView,
  Alert,
  Modal,
  Pressable
} from "react-native";
import {
  Container,
  CardItem,
  Header,
  Content,
  Left,
  Footer,
  Body,
  Right,
  Button,
  Title,
  Text,
  DatePicker,
  Item,
  Input,
  Spinner,
} from "native-base";
// import { Icon } from 'react-native-elements';
import DateTimePicker from "@react-native-community/datetimepicker";
import { SearchBar } from 'react-native-elements';
import { useSelector, useDispatch } from "react-redux";
import * as ApiDataAction from "../store/actions/ApiData";
//mport shortid from "shortid";
import Autocomplete from "react-native-autocomplete-input";
import Colors from "../ColorCodes/Colors";
import URL from "../api/ApiURL";
import Ionicons from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import AntDesign from "react-native-vector-icons/AntDesign";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import Card from "../components/Card";

import { useRoute, useFocusEffect } from "@react-navigation/native";
import { useIsFocused } from "@react-navigation/native";
import DropdownAlert from 'react-native-dropdownalert';

import AsyncStorage from "@react-native-community/async-storage";
import CartItem from "../components/CartItem";
import * as cartActions from "../store/actions/OrderBox";
import { connect } from "react-redux";
import { BottomSheet } from "react-native-btr";
import MyHeader from "../components/MyHeader";
import PreviewCart from '../components/PreviewCart';


function CreateNewOrder({ navigation ,route }) {
  const isFocused = useIsFocused();
  const {id, name ,address} = route.params
  
  const cartTotalAmount = useSelector((state) => state.OrderBox.totalAmount);
  const cartTotalPackages = useSelector((state) => state.OrderBox.totalPackages);
  const count = useSelector((state) => state.OrderBox.count);
  const CheckId = useSelector((state) => state.OrderBox.cardItemsArray);
  const cardItemsArray = useSelector((state) => {return state.OrderBox.cardItemsArray});
 
  
  var Count = 0;

  const dispatch = useDispatch();
  const ClientId = useSelector((state) => state.ApiData.ClientId);
  const ClientName = useSelector((state) => state.ApiData.ClientName);

  //const [currentDate, setCurrentDate] = useState("");
  const units = useSelector((state) => state.ApiData.ProductList);
  const products = useSelector((state) => state.ApiData.ProductList);


  const PoNumber = useSelector((state) => state.ApiData.PoNumber);
  const OrderId = useSelector((state) => state.ApiData.OrderId);
  console.log("cartItems  ", cardItemsArray);
  console.log("OrderId", OrderId);
  const [pickUpDate, setPickUpDate] = useState("");
  const [MyOrderBoxId, setMyOrderBoxId] = useState("");
  const [currentDate, setCurrentDate] = useState("");
  const [note, setNote] = useState("");
  const [qtty, setQtty] = useState(0);
  // const autocompletes = [...Array(10).keys()];
  // const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [selectedValue, setSelectedValue] = useState([{}]);

  // const [units, setUnits] = useState([]);
  const [totalAmount, setTotalAmount] = useState("");
  const [filteredUnits, setFilteredUnits] = useState([]);
  const [selectedUnits, setSelectedUnits] = useState({});
  const [checkRow, setCheckRow] = useState(false);
  const [unitCheck, setUnitCheck] = useState(false);
  const [riderData, setRiderData] = useState("");
  const [addressCheck,setAddressCheck]=useState(false);

  const [riderName, setRiderName] = useState("");
  const [riderAddress, setRiderAddress] = useState("");
  const [riderId, setRiderId] = useState("");
  const [formattedDate, setFormattedDate] = useState("");
  const [businessData, setBusinessData] = useState("");
  const [selectedBusinessId, setSelectedBusinessId] = useState("");
  const [loading, setLoading] = useState(false);
  const [riderLoading, setRiderLoading] = useState(false);
  const [AddressName, setAddressName] = useState("");
  const [businessName, setBusinessName] = useState("");
  // const [time,setTime]=useState("12:56:00");
  const [formattedTime, setFormattedTime] = useState("");
  const [time, setTime] = useState("");
  const [buttonState, setButtonState] = useState("");
  const [sendButtonCheck, setSendButtonCheck] = useState(false);
  const [todayDate,setTodayDate]=useState("");
  const [todayTime,setTodayTime]=useState("");
  const [modalVisible, setModalVisible] = useState(false);

 
  // const [sendButtonCheck, setSendButtonCheck] = useState("");
  

  var Datee;
  var Month;
  var Year;
  var Hour;
  var Minute;
  var Second;

  var datee;
  var monthh;
  var yearr;

  var hourss;
  var minn;
  var secc;

 
  const [date, setDate] = useState(new Date());
  const [wakt, setWakt] = useState(new Date());
  const [mode, setMode] = useState("datetime");
  const [show, setShow] = useState(false);






  const onChange = (event, selectedDate) => {
    const currentDate = selectedDate || date;
    setShow(Platform.OS === "ios");
    setDate(currentDate);
    // console.log("Dateeeeeeeee: ",currentDate.getDate());
    setFormattedDate(
      currentDate.getDate() +
          "-" +
          (currentDate.getMonth() + 1) +
          "-" +
          currentDate.getFullYear()
      );
      setFormattedTime(
        currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds()
      );
      console.log("updates Date",formattedDate);
      console.log("updates Time",formattedTime);
    // console.log("Timeeeeeeeee: ",Time);
  };

  const onChange1 = (event, selectedDate) => {
    const currentDate = selectedDate || date;
    setShow(Platform.OS === "ios");
    setDate(currentDate);
    // console.log("Dateeeeeeeee: ",currentDate.getDate());
   
      setFormattedTime(
        currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds()
      );
      // console.log("updates Date",formattedDate);
      console.log("updates Time",formattedTime);
    // console.log("Timeeeeeeeee: ",Time);
  };


  const showMode = (currentMode) => {
    setShow(true);
    setMode(currentMode);
  };

  const showDatepicker = () => {
    showMode("date");
  };

  const showTimepicker = () => {
    showMode("time");
  };

  const [visible, setVisible] = useState(false);
  const toggleBottomNavigationView = () => {
    //Toggling the visibility state of the bottom sheet
    setVisible(!visible);
  };

  const [s_visible, setS_visible] = useState(false);
  const s_toggleBottomNavigationView = () => {
    //Toggling the visibility state of the bottom sheet
    setS_visible(!s_visible);
  };

  const addOrderBox=()=>{
    setLoading(true);
    console.log("before Order box", OrderId);
    Count = Count + 1;
    setSendButtonCheck(true);
    setModalVisible(!modalVisible);
    fetch(URL + "/order/add_to_order_box/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        order_box: OrderId,
        order_products: cardItemsArray,
        
      }),
    })
      .then(async (response) => {
        let data = await response.json();
        // console.log("status code",response.status)
        // console.log("Order Detail",data.order_box.order_products)
        console.log("response.status",response.status)
        if (response.status == 201) {
          // console.log("data",data)
          // dispatch(ApiDataAction.CreateOrder(1));
          
          CreateOrder();
          console.log("(Oreder is added to order box)");
          // dispatch(ApiDataActions.SetLoginData(data));
          // navigation.navigate("MyDrawer");
        }
        else{
    setSendButtonCheck(false);
          alert(data.message)
          
        }

      })
      .catch((error) => {
        setSendButtonCheck(false);
        console.log("Something went wrong from add to order box", error);
      });
  }


  const CreateOrder = () => {
    setLoading(true);
    fetch(URL + "/order/create_order/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        order_box: OrderId,
        purchase_order_no: PoNumber,
        order_title: "Grocery",
        delivery_person:riderId==""?id:riderId,
        order_delivery_datetime: formattedDate==""?todayDate + " " + todayTime:formattedDate + " " + formattedTime,
        business_id: selectedBusinessId,
        delivery_notes: note,
        comment: "note",
        distance: "2km",
        status: "Pending",
        payment_type: "cash_on_delivery",
      }),
    })
      .then(async (response) => {
        let data = await response.json();
        // console.log("status code", response.status);
        // console.log("status code", data);
        if (response.status == 201) {
          // console.log("Create response",data.order.order_products)

          setLoading(false);
          // Alert.showAlert();
          alert("Thanks, your order has been placed.");
          // dropDownAlertRef.alertWithType('success', 'Success', 'Your Order Has Been Placed.');
          // Toast.show("Your Order Has Been Placed.", Toast.LONG);
          dispatch(cartActions.allClear(1));
          dispatch(ApiDataAction.Clear(1));
          setSelectedValue([{}]);
          setNote("");
          setUnitCheck(false);
          setQtty("");
          setFormattedDate("");
          // AsyncStorage.clear();
          
          navigation.navigate("Dashboard");

          setSendButtonCheck(false);

          // dispatch(ApiDataActions.SetLoginData(data));
          // navigation.navigate("MyDrawer");
        } else {
          alert(data.message)
          // Toast.show(data.message, Toast.LONG);

          // alert("Unable to Create Order");
          setLoading(false);
          setSendButtonCheck(false);
        }

        // code that can access both here
      })
      .catch((error) => {
        console.log("Something went wrong at create order Box", error);
        setLoading(false);
        setSendButtonCheck(false);
      });
  };




  const sendOrder = () => {
   
    setFormattedDate(
        date.getDate() +
          "-" +
          (date.getMonth() + 1) +
          "-" +
          date.getFullYear()
      );
      setFormattedTime(
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds()
      );
      console.log("updates Dateeeeeeeeeeeeeeeeeeeeeee   ",formattedDate);
      console.log("updates Timeeeeeeeeeeeeeeeeeeeeeee   ",formattedTime);
    // AsyncStorage.clear();
    // dispatch(ApiDataAction.SetOrderBoxId(1));
    // console.log("value",selectedValue.id);
    if (cardItemsArray == "") {
      
      alert("Kindly place an order.");
    } else {
    
      if (selectedBusinessId == "") {
       
        alert("Please select delivery address");

      }
      else{
        setModalVisible(!modalVisible)
       
      }
        
      
    }

    // alert("Thanks,Your Order is Placed,")
  };

  


  const findName = (query) => {
    //method called everytime when we change the value of the input
    if (query) {
      //making a case insensitive regular expression to get similar value from the film json
      const regex = new RegExp(`${query.trim()}`, "i");
      //setting the filtered film array according the query from the input
      setFilteredProducts(
        products.filter((product) => product.name.search(regex) >= 0)
      );
    } else {
      //if the query is null then return blank
      setFilteredProducts([]);
    }
  };
  const findUnit = (query) => {
    //method called everytime when we change the value of the input
    if (query) {
      //making a case insensitive regular expression to get similar value from the film json
      const regex = new RegExp(`${query.trim()}`, "i");
      //setting the filtered film array according the query from the input
      setFilteredUnits(units.filter((uni) => uni.unit.search(regex) >= 0));
    } else {
      //if the query is null then return blank
      setFilteredUnits([]);
    }
  };

  const rider = (name, address, id) => {
    setRiderName(name);
    setRiderAddress(address);
    setRiderId(id);
    toggleBottomNavigationView();
  };
  // alert(e);
  // });

  useEffect(() => {

    // setProducts(productData);
    // setUnits(productData);


    fetch(URL + "/client_app/list_business/client/" + ClientId + "/")
      // fetch(URL+'/client_app/clients_list/33/')
      .then((response) => response.json())
      .then((responseJson) => {
        
        setBusinessData(responseJson.client_businesses);
        setAddressCheck(false);

        if (responseJson.client_businesses == "") {
          setAddressCheck(true);
          // setLoading(true);
        }
        // console.log("Business Detail", responseJson);
        // }
      })
      .catch((error) => console.error(error));

   

    LogBox.ignoreLogs(["VirtualizedLists should never be nested"]);
    LogBox.ignoreLogs(["Possible Unhandled Promise Rejection"]);
    LogBox.ignoreLogs(["Failed child context type"]);
    LogBox.ignoreLogs(["Failed prop type"]);

    fetch(URL + "/delivery_person/delivery_person_list/")
      // fetch(URL+'/client_app/clients_list/33/')
      .then((response) => response.json())
      .then((responseJson) => {
        if (responseJson.delivery_person == "") {
          setRiderLoading(true);
        } else {
          setRiderData(responseJson.delivery_person);
        }

        
      })
      .catch((error) => console.error(error));

      
      


      
    datee = ("0" + new Date().getDate()).slice(-2); //Current Date
    // if(datee<10){
    //   datee="0"+datee;
    // }
    monthh = ("0" + (new Date().getMonth() + 1)).slice(-2)//Current Month
    // if(monthh<10){
    //   monthh="0"+monthh;
    // }
    console.log("Monthhhhhhhhhhhhhhhhhhhhh :",date)
    yearr = new Date().getFullYear(); //Current Year
    hourss = new Date().getHours(); //Current Hours
    minn = new Date().getMinutes(); //Current Minutes
    secc = new Date().getSeconds(); //Current Seconds
    console.log("date",datee);
    setCurrentDate(datee + "-" + monthh + "-" + yearr);
    setTodayDate(datee +"-" +monthh +"-" +yearr);
      setTodayTime(
        hourss + ":" + minn + ":" + secc
      );




      


      






  }, [checkRow, count, OrderId, isFocused, formattedDate, date]);


  useEffect(() => {

   return () => {
        dispatch(cartActions.allClear(1));
        // Clean up the subscription
      };
  },[]);

  var reg = /^\d+$/;
  return (
    <>
    
    <View style={{ flex: 1, backgroundColor: "white", height: "100%" }}>
      {/* <FlashMessage position="top" /> */}
      {/* <DropdownAlert ref={ref => dropDownAlertRef = ref} updateStatusBar={false} tapToCloseEnabled={true} errorColor={Colors.themeColor} containerStyle={{width:"80%"}} /> */}
      {/* <MyHeader name="CREATE NEW ORDER" nav={navigation} /> */}
      <KeyboardAvoidingView style={{ flex: 1 }}
        behavior={Platform.OS == "ios" ? "padding" : null} >
      <ScrollView
        style={{ padding: 0 }}
        nestedScrollEnabled={true}
        keyboardShouldPersistTaps="always"
        listViewDisplayed={false}
      >
        <View>

          <View style={{ height: "14%", padding: 5 }}>
            <Text
              style={{
                alignSelf: "center",
                flexDirection: "row",
                fontSize: 16,
                fontWeight: "bold",
              }}
            >
              {PoNumber}
            </Text>

            <View
              style={{ flexDirection: "row", alignSelf: "center", padding: 10 }}
            >
              <Card
                style={{
                  padding: 10,
                  width: "50%",
                  backgroundColor: "#e6e6e6",
                  elevation: 0,
                }}
              >
                <TouchableOpacity onPress={toggleBottomNavigationView}>
                  <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                    Delivery Person:
                  </Text>
                  {riderId==""?<Text style={{ fontSize: 16, fontWeight: "bold" }}>
                    {name}
                  </Text>:
                  <Text style={{ fontSize: 16, fontWeight: "bold" }}>
                  {riderName}
                </Text>}
                 {riderId==""?<Text style={{ fontSize: 12, color: "#666666" }}>
                    {address}
                  </Text>:
                  <Text style={{ fontSize: 12, color: "#666666" }}>
                    {riderAddress}
                  </Text>}
                </TouchableOpacity>
              </Card>
              <BottomSheet
                visible={visible}
                onBackButtonPress={toggleBottomNavigationView}
                onBackdropPress={toggleBottomNavigationView}
              >
               
                <View style={styles.bottomNavigationView}>
                  {riderLoading ? (
                    <View
                      style={{
                        justifyContent: "center",
                        alignItems: "center",
                        // alignSelf:'center',
                        marginTop: "20%",
                      }}
                    >
                      <Text
                        style={{
                          color: Colors.themeColor,
                          fontWeight: "bold",
                          marginTop: 20,
                          fontSize: 25,
                          textAlign: "center",
                        }}
                      >
                        Rider is Not Available
                      </Text>
                    </View>
                  ) : (
                    <FlatList
                      // nestedScrollEnabled={true}
                      data={riderData}
                      style={{ padding: 10,marginTop:Platform.OS=="android"?0:"12%" }}
                      showsVerticalScrollIndicator={false}
                      // keyExtractor={item => item.index_id.toString()}
                      keyExtractor={({ id }, index) => id}
                      renderItem={({ item }) => (
                        <TouchableOpacity
                          style={{
                            width: "95%",
                            marginBottom: 15,
                            alignSelf: "center",
                            
                          }}
                          onPress={() =>{
                            rider(
                              item.first_name + " " + item.last_name,
                              item.address,
                              item.id
                            )
                          }}
                           // onPress = {() => navigation.navigate("PendingDetails" , {Due_Date : item.due_date , Invoice_Total : item.grand_total,Carrier_Name : item.carrier_company ,Load_Type : item.load_type,Origin_City : item.Origin_city,Destination_City : item.Destination_city,Delivery_Option : item.Delivery_Option,Cargo_Amount : item.Cargo_amount,Cargo_Type : item.Cargo_Type,Cargo_Product_Type : item.Cargo_Product_type,Cargo_Product_List : item.Cargo_Product_List,Booking_Status : item.booking_status})}
                          // onPress={() => 
                           // navigation.navigate("PaymentHistoryDetail")
                          // }
                        >
                          <Card 
                             style={{
                              borderRadius: 15,
                              padding: 10,
                            }}
                          > 
                             <View
                              style={{ 
                               // borderRadius: 10,
                                // backgroundColor: "white",
                                // overflow: "hidden",

                                flexDirection: "column",
                                // justifyContent: "flex-start",
                                // alignSelf: "center",

                                // marginTop: 10,
                                // shadowColor: "#000",
                                // shadowOffset: { width: 0, height: 2 },
                                // shadowOpacity: 0.25,
                                // shadowRadius: 3.84,
                                // elevation: 5,
                              }}
                            > 
                              <View style={{ flexDirection: "row" }}>
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
                                      // marginTop: "4%",
                                    }}
                                  >
                                    {item.first_name} {item.last_name}
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
                                  <Text
                                    style={{
                                      marginBottom: 3,
                                      fontSize: 14,
                                      alignSelf: "flex-end",
                                      marginRight: 10,
                                      fontWeight: "bold",
                                    }}
                                  ></Text> 
                                   {/* <Text style={{ fontSize:12,alignSelf:'flex-end', color: "white",backgroundColor:Colors.darkRedColor,borderRadius:10,padding:5,}}>
  {item.status}
  </Text>  */}
                                 </View>
                              </View>
                            </View>
                          </Card>
                        </TouchableOpacity>
                      )}
                    />
                  )}
                </View>
              </BottomSheet> 

              <Card
                style={{
                  padding: 10,
                  marginLeft: 10,
                  width: "50%",
                  backgroundColor: "#e6e6e6",
                  elevation: 0,
                }}
              >
                <TouchableOpacity
                  // style={{width:"95%",marginBottom:15,alignSelf:'center'}}
                  // onPress={()=>rider(item.first_name+" "+item.last_name,item.address,item.id)}
                  onPress={s_toggleBottomNavigationView}
                >
                  <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                    Delivery Address:
                  </Text>
                  <Text style={{ fontSize: 16, fontWeight: "bold" }}>
                    {businessName}
                  </Text>
                  <Text style={{ fontSize: 12, color: "#666666" }}>
                    {AddressName}
                  </Text>
                </TouchableOpacity>
              </Card>

              <BottomSheet
                visible={s_visible}
                //setting the visibility state of the bottom shee
                onBackButtonPress={s_toggleBottomNavigationView}
                //Toggling the visibility state on the click of the back botton
                onBackdropPress={s_toggleBottomNavigationView}
                //Toggling the visibility state on the clicking out side of the sheet
              >
                {/*Bottom Sheet inner View*/}
                <View style={styles.bottomNavigationView}>
                  {addressCheck ? (
                    <View
                      style={{
                        justifyContent: "center",
                        alignItems: "center",
                        // alignSelf:'center',
                        marginTop: "60%",
                      }}
                    >
                      <Text
                        style={{
                          color: "black",
                          fontWeight: "bold",
                          marginTop: 20,
                          fontSize: 25,
                          textAlign: "center",
                        }}
                      >
                        There is no Address Record, Please Add Your Address.
                      </Text>
                      <View style={{ marginTop: 40 }}>
        <TouchableOpacity
          style={styles.uploadButton}
          activeOpacity={0.7}
          onPress={() => {s_toggleBottomNavigationView(); navigation.navigate("NewBuisnessDetail")}}
        >
          <Text style={styles.uploadButtonText}>Add New Business</Text>
        </TouchableOpacity>
      </View>
                    </View>
                  ) : (
                    <FlatList
                      nestedScrollEnabled={true}
                      data={businessData}
                      style={{ padding: 10,marginTop:Platform.OS=="android"?0:"12%" }}
                      showsVerticalScrollIndicator={false}
                      // keyExtractor={item => item.index_id.toString()}
                      keyExtractor={({ id }, index) => id}
                      renderItem={({ item }) => (
                        <View>
                          <TouchableOpacity
                            style={{
                              width: "95%",
                              marginBottom: 15,
                              alignSelf: "center",
                            }}
                            onPress={() => {
                              setSelectedBusinessId(item.id);
                              setAddressName(item.address);
                              setBusinessName(item.name);
                              s_toggleBottomNavigationView();
                            }}
                            // onPress = {() => navigation.navigate("PendingDetails" , {Due_Date : item.due_date , Invoice_Total : item.grand_total,Carrier_Name : item.carrier_company ,Load_Type : item.load_type,Origin_City : item.Origin_city,Destination_City : item.Destination_city,Delivery_Option : item.Delivery_Option,Cargo_Amount : item.Cargo_amount,Cargo_Type : item.Cargo_Type,Cargo_Product_Type : item.Cargo_Product_type,Cargo_Product_List : item.Cargo_Product_List,Booking_Status : item.booking_status})}
                            // onPress={() =>
                            // navigation.navigate("PaymentHistoryDetail")
                            // }
                          >
                            <Card style={{ borderRadius: 15, padding: 10 }}>
                              <View
                                style={{
                                  // borderRadius: 10,
                                  // backgroundColor: "white",
                                  // overflow: "hidden",

                                  flexDirection: "column",
                                  // justifyContent: "flex-start",
                                  // alignSelf: "center",

                                  // marginTop: 10,
                                  // shadowColor: "#000",
                                  // shadowOffset: { width: 0, height: 2 },
                                  // shadowOpacity: 0.25,
                                  // shadowRadius: 3.84,
                                  // elevation: 5,
                                }}
                              >
                                <View style={{ flexDirection: "row" }}>
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
                                        // marginTop: "4%",
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
                                    <Text
                                      style={{
                                        marginBottom: 3,
                                        fontSize: 14,
                                        alignSelf: "flex-end",
                                        marginRight: 10,
                                        fontWeight: "bold",
                                      }}
                                    ></Text>
                                    {/* <Text style={{ fontSize:12,alignSelf:'flex-end', color: "white",backgroundColor:Colors.darkRedColor,borderRadius:10,padding:5,}}>
  {item.status}
  </Text> */}
                                  </View>
                                </View>
                              </View>
                            </Card>
                          </TouchableOpacity>
                        </View>
                      )}
                    />
                  )}
                </View>
              </BottomSheet>










              













            </View>
          </View>
          <Modal
        animationType="slide"
        
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => {
        //   Alert.alert("Modal has been closed.");
          setModalVisible(!modalVisible);
        }}
      >
        <View style={styles.centeredView2}>
          <View style={styles.modalView2}>
          <View style = {{width:"95%",height:Platform.OS=="android"?"95%":"90%",backgroundColor:'white',alignSelf:"center",borderRadius:10,flexDirection:'row',
          shadowColor: "#000",
          shadowOffset: { width: 0, height: 2 },
          // shadowOpacity: 0.25,
          shadowRadius: 3.84,
          elevation: 0,
          }}>
            {/* <Card style={{borderRadius:10,width:"90%",height:"90%",alignItems:'center',backgroundColor:"white"}}> */}
              <ScrollView keyboardShouldPersistTaps="always"  showsVerticalScrollIndicator={false} style={{padding:10}}>
            <View style={{alignSelf:"center",padding:"3%",paddingBottom:"2%",marginRight:10}}>
              <Text style={{color:Colors.themeColor,fontSize:24,fontWeight:"bold",textAlign:"center"}}>PREVIEW</Text>
            </View>
            <View style={{ flexDirection: "row",padding:5,alignSelf:"center" }}>
            <View style = {{width:"50%",backgroundColor:'#e6e6e6',alignSelf:"center",borderRadius:10,
          shadowColor: "#000",
          shadowOffset: { width: 0, height: 2 },
          // shadowOpacity: 0.25,
          shadowRadius: 3.84,
          elevation: 0,
          padding:10
          }}>
            
            {/* <Card
                style={{
                  padding: 10,
                  width: "48%",
                  backgroundColor: "#e6e6e6",
                  elevation: 0,
                }}
              > */}
                
                  <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                    Delivery Person:
                  </Text>
                  {riderId==""?<Text style={{ fontSize: 16, fontWeight: "bold" }}>
                    {name}
                  </Text>:
                  <Text style={{ fontSize: 16, fontWeight: "bold" }}>
                  {riderName}
                </Text>}
                 {riderId==""?<Text style={{ fontSize: 12, color: "#666666" }}>
                    {address}
                  </Text>:
                  <Text style={{ fontSize: 12, color: "#666666" }}>
                    {riderAddress}
                  </Text>}
                
              </View>
              <View style = {{width:"50%",backgroundColor:'#e6e6e6',alignSelf:"center",borderRadius:10,
          shadowColor: "#000",
          shadowOffset: { width: 0, height: 2 },
          // shadowOpacity: 0.25,
          shadowRadius: 3.84,
          elevation: 0,
          padding:10,
          marginLeft:5
          }}>
                
                  <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                    Delivery Address:
                  </Text>
                  <Text style={{ fontSize: 16, fontWeight: "bold" }}>
                    {businessName}
                  </Text>
                  <Text style={{ fontSize: 12, color: "#666666" }}>
                    {AddressName}
                  </Text>
                
              </View>
              </View>

{/* //-------------- changing in date time UI-----------// */}
{/* {Platform.OS === "ios"? ( */}
  <View
  style={{
    flexDirection: "row",
    alignSelf: "center",
    padding: 5,
    paddingTop:0
  }}
>
  

  <View style = {{width:"50%",backgroundColor:'#e6e6e6',alignSelf:"center",borderRadius:10,
shadowColor: "#000",
shadowOffset: { width: 0, height: 2 },
// shadowOpacity: 0.25,
shadowRadius: 3.84,
elevation: 0,
padding:10,

}}>
    <View style={{ padding: 5 }}>
      
        <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
          Delivery Date:
        </Text>
        <Text
          style={{
            fontSize: 16,
            fontWeight: "bold",
            textAlign: "center",
          }}
        >
          {("0" + date.getDate()).slice(-2) +
            "-" +
            ("0" + (date.getMonth() + 1)).slice(-2)+
            "-" +
            date.getFullYear()}
        </Text>
      
    </View>
  </View>

  <View style = {{width:"50%",backgroundColor:'#e6e6e6',alignSelf:"center",borderRadius:10,
shadowColor: "#000",
shadowOffset: { width: 0, height: 2 },
// shadowOpacity: 0.25,
shadowRadius: 3.84,
elevation: 0,
padding:10,
marginLeft:5
}}>
    <View style={{ padding: 5 }}>
      
        <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
          Delivery Time:
        </Text>
        <Text
          style={{
            fontSize: 16,
            fontWeight: "bold",
            textAlign: "center",
          }}
        >
          {("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2)}
          {/* {("0" + wakt.getHours()).slice(-2) + ":" + ("0" + wakt.getMinutes()).slice(-2)} */}
        </Text>
      
    </View>
  </View>
</View>
 
 

              

              
              <View style={{flexDirection:'row',marginTop:10}}>
        <Text style={{color:Colors.themeColor,fontWeight:"bold",marginLeft:"2%",width:"31%",textAlign:"left"}}>Product</Text>
        <Text style={{color:Colors.themeColor,fontWeight:"bold",textAlign:"center",width:"15%"}}>Unit</Text>
        <Text style={{color:Colors.themeColor,fontWeight:"bold",textAlign:"center",width:"24%"}}>Quantity</Text>
        <Text style={{color:Colors.themeColor,fontWeight:"bold",textAlign:"right",width:"26%"}}>Last month Avg.Price</Text>
    </View>
    <View style={{padding:2}}>
              <FlatList
                          nestedScrollEnabled
                          data={cardItemsArray}
                          // sort={true}
                          // inverted={true}
                          keyExtractor={(item) => item.id}
                          renderItem={(itemData) => (
                            <PreviewCart
                              id={itemData.item.id}
                              quantity={itemData.item.quantity}
                              total_amount={itemData.item.total_amount}
                              name={itemData.item.name}
                              unit={itemData.item.unit}
                              price={itemData.item.price}
                              // addable
                              onAddPress={() => {
                                dispatch(

                                  cartActions.addToQtty(itemData.item.id)
                                );
                              }}
                              // deletable
                              onRemove={() => {
                                dispatch(
                                  cartActions.removeFromCart(itemData.item.id)
                                );
                              }}
                              // removeable
                              onDelete={() => {
                                dispatch(
                                  cartActions.deleteProduct(itemData.item.id)
                                );
                              }}
                            />
                          )}
                        />
              </View>
              <View style={{ flexDirection: "row", }}>
                    <Text
                      style={{ color: Colors.themeColor,fontWeight:'bold',width:"51%",marginLeft:"2%",textAlign:"left"}}
                    >
                      Total:
                    </Text>
                    <Text style={{ color: Colors.themeColor, fontWeight:'bold',width:"15%",textAlign:"center" }}>
                      {cartTotalPackages}
                    </Text>
                    {cartTotalAmount==0?<Text style={{ color: Colors.textGreyColor,width:"26%",textAlign:"right" }}>
                    £ {cartTotalAmount}
                    </Text>:
                    <Text style={{ color: Colors.textGreyColor,width:"26%",textAlign:"right" }}>
                    £ {parseFloat(cartTotalAmount).toFixed(2)}
                    </Text>}
                  </View>


                  {note==""?null:
                <View style={{alignSelf:"center",paddingTop:"20%"}}>
                  <Text>Note: {note}</Text>
                </View>}


          <View style={{marginTop:"10%",alignSelf:"center"}}>
            <Pressable
               style={styles.signupButton1}
               activeOpacity={0.7}
              onPress={addOrderBox}
            >
              {
              loading ? (
                <Spinner color={"white"} size={20} />
              ) : (
              <Text style={styles.signupButtonText1}>CONFIRM</Text>)}
            </Pressable>
            <Pressable
               style={{...styles.bu_signupButton1,borderWidth:1,marginBottom:"10%"}}
               activeOpacity={0.7}
              onPress={()=>
                setModalVisible(!modalVisible)
                }
            >
              <Text style={styles.bu_signupButtonText1}>CANCEL</Text>
            </Pressable>
            </View>
            </ScrollView>
           </View>
        
 
            
          </View>
        </View>
      </Modal>

          <View style={{ height: "70%", marginTop: 40}}>
            <Card
              style={{
                padding: 10,
                width: "100%",
                backgroundColor: "#e6e6e6",
                elevation: 0,
                //marginBottom:'15%'
              }}
            >
              <Text
                style={{
                  alignSelf: "center",
                  flexDirection: "row",
                  fontSize: 14,
                  // fontWeight: "bold",
                }}
              >
                Order Date
              </Text>
              <Text
                style={{
                  alignSelf: "center",
                  flexDirection: "row",
                  fontSize: 15,
                  fontWeight: "bold",
                  color: Colors.themeColor,
                }}
              >
                {currentDate}
              </Text>
              
  


{ Platform.OS==='ios'? (

<View
                style={{
                  flexDirection: "row",
                  alignSelf: 'center',
                  padding: 5,
                }}
              >

    {/* //-------------------------------------Delivery Date ----------------------------// */}            
<Card
                  style={{
                    padding: 5,
                    // marginLeft: 10,
                    width: "90%",
                    backgroundColor: "#F2F2F2",
                    elevation: 0,
                    flexDirection:'row',
                    marginBottom:'5%',
                    marginTop:'5%'
                  }}
                >
                  <View style={{ padding: 7 ,
                    marginRight:'5%' 
                    }}>
                    <TouchableOpacity onPress={showDatepicker}>
                      <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                        Delivery Date
                      </Text>
                      <Text
                        style={{
                          fontSize: 16,
                          fontWeight: "bold",
                          textAlign: "center",
                        }}
                      >

                        
                        {("0" + date.getDate()).slice(-2) +
                          "-" +
                          ("0" + (date.getMonth() + 1)).slice(-2)+
                          "-" +
                          date.getFullYear()}
                      </Text>
                    </TouchableOpacity>
                    
                  </View>
                {/* </Card> */}

                {/* //-------------------------------------Delivery Time ----------------------------// */}
               

                  <View style={{ alignSelf:'flex-end', width:'30%'  }}>
                  {show && (
                      
                      <DateTimePicker
                        testID="dateTimePicker"
                        value={date}
                        mode={mode}
                        // defaultDate={new Date()}
                        minimumDate={new Date()}
                        is24Hour={true}
                        style={{ color: Colors.themeColor }}
                        display="default"
                        // dateFormat="day month year"
                        onChange={onChange}
                      />
                    )}
                  </View>



                  {/* <View style={{ alignSelf:'flex-end', width:'30%'  }}>
                  {show && (
                      
                      <DateTimePicker
                        testID="dateTimePicker"
                        value={formattedTime}
                        mode={mode}
                        // defaultDate={new Date()}
                        //minimumDate={new Date()}
                        is24Hour={true}
                        style={{ color: Colors.themeColor }}
                        display="default"
                        // dateFormat="day month year"
                        onChange={onChange1}
                      />
                    )}
                  </View> */}



                  <View
                style={{
                  flexDirection: "row",
                  //alignSelf: 'flex-start',
                  alignItems:'flex-end',
                  marginLeft:'3%',
                  padding: 7,
                }}
              >
                    <TouchableOpacity onPress={showTimepicker}>
                      <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                        Delivery Time
                      </Text>
                      <Text
                        style={{
                          fontSize: 16,
                          fontWeight: "bold",
                          textAlign: "center",
                        }}
                      >
                        {("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2)}
                      </Text>
                    </TouchableOpacity>
                    
                  </View>
                </Card>

              </View>

):(

<View
                style={{
                  flexDirection: "row",
                  alignSelf: "center",
                  padding: 5,
                }}
              >

                {/* //-------------------------------------Delivery Date ----------------------------// */}
<Card
                  style={{
                    padding: 5,
                    // marginLeft: 10,
                    width: "50%",
                    backgroundColor: "#F2F2F2",
                    elevation: 0,
                  }}
                >
                  <View style={{ padding: 5 }}>
                    <TouchableOpacity onPress={showDatepicker}>
                      <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                        Delivery Date:
                      </Text>
                      <Text
                        style={{
                          fontSize: 16,
                          fontWeight: "bold",
                          textAlign: "center",
                        }}
                      >
                        {("0" + date.getDate()).slice(-2) +
                          "-" +
                          ("0" + (date.getMonth() + 1)).slice(-2)+
                          "-" +
                          date.getFullYear()}
                      </Text>
                    </TouchableOpacity>

                    {show && (
                      
                      <DateTimePicker
                        testID="dateTimePicker"
                        value={date}
                        mode={mode}
                        // defaultDate={new Date()}
                        minimumDate={new Date()}
                        is24Hour={true}
                        style={{ color: Colors.themeColor }}
                        display="default"
                        // dateFormat="day month year"
                        onChange={onChange}
                      />
                    )}

                  </View>
                </Card>

                {/* //-------------------------------------Delivery Time ----------------------------// */}
                <Card
                  style={{
                    padding: 5,
                    marginLeft: 10,
                    width: "50%",
                    backgroundColor: "#F2F2F2",
                    elevation: 0,
                  }}
                >
                  <View style={{ padding: 5 }}>
                    <TouchableOpacity onPress={showTimepicker}>
                      <Text style={{ color: Colors.themeColor, fontSize: 12 }}>
                        Delivery Time:
                      </Text>
                      <Text
                        style={{
                          fontSize: 16,
                          fontWeight: "bold",
                          textAlign: "center",
                        }}
                      >
                        {("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2)}
                      </Text>
                    </TouchableOpacity>
                  </View>
                </Card>

              </View>

) }



              
              <Text
                style={{
                  color: Colors.themeColor,
                  fontSize: 14,
                  fontWeight: "bold",
                  alignSelf: "center",
                  marginTop: 10,
                }}
              >
                Add Item and Quantity Here:
              </Text>

              <View
                style={{
                  flexDirection: "row",
                  marginTop: "5%",
                  width: "100%",
                }}
              >
               <View
                  style={{
                    width: Platform.OS == "android" ? "30%" : "30%",
                    
                  }}
                >
                  <Autocomplete
                    // onFocus={() => {scrollView.props.scrollToEnd({animated: true})}}
                    autoCapitalize="none"
                    autoCorrect={false}
                    flatListProps={{ nestedScrollEnabled: true}}
                    // containerStyle={{}}
                   
                    listContainerStyle={{
                      backgroundColor: "#e6e6e6",
                      width: 250,
                      left: 0,
                      position: 'absolute',
                      right: 0,
                      top: 50,
                    zIndex: 1,
                      // height: Platform.OS == "android" ? 150 :150

                    }}
                    listStyle={{
                      borderColor: "#e6e6e6",
                      height: Platform.OS == "android" ? 150 :150,
                    }}
                    style={{
                      // backgroundColor: "#e6e6e6",
                      paddingBottom: 7,
                      color: "black",
                      width: "100%",
                    }}
                    inputContainerStyle={{
                      backgroundColor: "#F2F2F2",
                      height: Platform.OS == "android" ? 45 : 40,
                      justifyContent: "center",

                      //borderColor: "#e6e6e6",
                      //borderBottomColor: Colors.textGreyColor,
                    }}
                    //data to show in suggestion
                    data={filteredProducts}
                    //default value if you want to set something in input
                    defaultValue={
                      JSON.stringify(selectedValue) === "{}"
                        ? ""
                        : selectedValue.name
                    }
                    // onchange of the text changing the state of the query
                    // which will trigger the findFilm method
                    // to show the suggestions
                    onChangeText={(text) => findName(text)}
                    placeholder="Add Item"
                    placeholderTextColor="black"
                    renderItem={({ item }) => (
                      <ScrollView keyboardShouldPersistTaps="always">
                        <TouchableOpacity
                          // style={{paddingHorizontal:10}}

                          onPress={() => {
                            setSelectedValue(item);
                            setFilteredProducts([]);
                            setUnitCheck(true);
                          }}
                        >
                          <Text style={styles.itemText}>
                            {item.name} ({item.unit})
                          </Text>
                        </TouchableOpacity>
                      </ScrollView>
                    )}
                  />
                </View>

                <View style={{ width: "20%", height: 38, paddingTop: 5 }}>
                  {unitCheck ? (
                    <Text
                      style={{
                        color: Colors.textGreyColor,
                        marginLeft: 1,
                        padding: 10,
                        paddingBottom: 12.5,
                      }}
                    >
                      {selectedValue.unit}
                    </Text>
                  ) : (
                    <Text
                      style={{
                        color: Colors.textGreyColor,
                        marginLeft: 1,
                        padding: 10,
                        paddingBottom: 12.5,
                      }}
                    >
                      Unit
                    </Text>
                  )}
                </View>
                <View style={{ width: "15%", paddingTop: 0 }}>
                  <TextInput
                    style={styles.o_inputArea}
                    placeholder="Qty"
                    autoCapitalize="none"
                    keyboardType="numeric"
                    maxLength={2}
                    placeholderTextColor="black"
                    value={qtty}
                    required={true}
                    onChangeText={(value) => setQtty(value)}
                    initialValue=""
                  />
                </View>

                {unitCheck ? (
                  <View style={{ width: "28%", paddingTop: 5 }}>
                    <Text
                      style={{
                        color: Colors.textGreyColor,
                        padding: 10,
                        marginLeft: 1,
                        paddingBottom: 12.5,
                      }}
                    >
                      £ {selectedValue.avg_price}
                    </Text>
                  </View>
                ) : (
                  <View style={{ width: "40%", paddingTop: 0 }}>
                    <Text
                      style={{
                        color: Colors.textGreyColor,
                        padding: 10,
                        paddingTop:0,
                        marginLeft: 1,
                        paddingBottom: 12.5,
                      }}
                    >
                    Last month Avg.Price
                    </Text>
                  </View>
                )}

                <View
                  style={{
                    height: 30,
                    width: "6%",
                    alignSelf: "center",
                    justifyContent: "center",
                    marginLeft: 0,
                  }}
                >
                  {unitCheck ? (
                    <TouchableOpacity
                      activeOpacity={0.8}
                      style={styles.AddButton}
                      onPress={() => {
                        const userExists = CheckId.some(item => item.id === selectedValue.id);
                        console.log('statuuuuuuuuuuuuuuuuuuuuuuus',userExists);
                        if (userExists) {
                            // dropDownAlertRef.alertWithType('error', '', "Already Inserted");
                          // console.log('status',status);
                          alert("Already inserted");
                        } else {
                          if (qtty == "") {
                            // dropDownAlertRef.alertWithType('error', '', "Please Enter Quantity.");

                            alert("Please enter quantity.");
                          }
                          else if(reg.test(qtty) === false) {

                            alert("Invalid quantity");
                            setQtty("");
                              return false;
                          }
                          else if(qtty==0) {

                            alert("Invalid quantity");
                            setQtty("");
                          }
                          else {
                            dispatch(
                              cartActions.addToCart(selectedValue, qtty)
                            ),
                              setCheckRow(true),
                              setSelectedValue([{}]),
                              setUnitCheck(false),
                              setQtty("");
                          }
                        }
                      }}
                    >
                      <Text
                      style={styles.AddButtonText}
                      >
                        ADD
                      </Text>
                      {/* <AntDesign name="pluscircleo" color={Colors.themeColor} size={20} style={{padding:10}} /> */}
                    </TouchableOpacity>
                  ) : null}
                </View>

                {/* <View style={styles.container}> */}

                {/* </View> */}
              </View>

              {/* </Card> */}
              {/* </View> */}

              {/* <View style={{padding:10,height:'60%',marginTop:30}}> */}
              {/* <Card style={{elevation:0 ,backgroundColor:'#E6E6E6'}}> */}
              {/* <Text style={styles.verticleLine}></Text> */}

              <View
                style={{
                  borderRadius: 10,
                  backgroundColor: "#F2F2F2",
                  padding: 10,
                  marginTop: 20,
                  zIndex:-1
                }}
              >
                
                <View style = {{height:"60%",backgroundColor:'#F2F2F2',alignSelf:"center",borderRadius:10,
          shadowColor: "#000",
          shadowOffset: { width: 0, height: 2 },
          // shadowOpacity: 0.25,
          shadowRadius: 3.84,
          elevation: 0,
          padding:10,
          
          // marginLeft:5
          }}>
                  <View>
                    <View
                      style={{
                        flexDirection: "row",
                        marginTop: 10,
                        //justifyContent: "center",
                        width: "100%",
                      }}
                    >
                      <Text
                        style={{
                          color: Colors.themeColor,
                          width: "30%",
                          textAlign: "center",

                          fontSize: 14,
                        }}
                      >
                        Product
                      </Text>
                      <Text
                        style={{
                          color: Colors.textGreyColor,
                          width: "20%",
                          textAlign: "center",

                          fontSize: 14,
                        }}
                      >
                        Unit
                      </Text>
                      <Text
                        style={{
                          color: Colors.themeColor,
                          width: "20%",

                          fontSize: 14,
                          textAlign: "center",
                        }}
                      >
                        Quantity
                      </Text>
                      <Text
                        style={{
                          color: Colors.textGreyColor,
                          width: "28%",

                          fontSize: 14,
                          textAlign:"center",
                        }}
                      >
                        Last month Avg.Price
                      </Text>

                      {/* <SafeAreaView> */}
                      {/* <View style={styles.container}> */}

                      {/* </View> */}
                      {/* </SafeAreaView> */}
                    </View>
                    <View style={{}}>
                      {/* <ScrollView nestedScrollEnabled > */}
                     {checkRow ?  (
                        
                        <FlatList
                          nestedScrollEnabled
                          // inverted
                          // style={{flexDirection:"column-reverse"}}
                          keyboardShouldPersistTaps={'handled'}
                          contentContainerStyle={{paddingBottom:90}}
                          data={cardItemsArray}
                          // sort={true}
                          // inverted={true}
                          keyExtractor={(item) => item.id}
                          renderItem={(itemData) => (
                            // <Text style={{fontSize:30,backgroundColor:"green",flex:1}}>{JSON.stringify(itemData)}</Text>
                            // <View style={{flexDirection:"column-reverse"}}>
                            <CartItem
                              id={itemData.item.id}
                              quantity={itemData.item.quantity}
                              total_amount={itemData.item.total_amount}
                              name={itemData.item.name}
                              unit={itemData.item.unit}
                              price={itemData.item.price}
                              
                              // addable
                              onAddPress={() => {
                                dispatch(
                                  cartActions.addToQtty(itemData.item.id)
                                );
                              }}
                              // deletable
                              onRemove={() => {
                                dispatch(
                                  cartActions.removeFromCart(itemData.item.id)
                                );
                              }}
                              // removeable
                              onDelete={() => {
                                dispatch(
                                  cartActions.deleteProduct(itemData.item.id)
                                );
                              }}
                            />
                            // </View>
                          )}
                        />
                      ) : null
                      }
                      {/* </ScrollView> */}
                      <View style={{flexDirection: "row", paddingTop:10,paddingBottom:0 ,borderBottomWidth:.5 , borderBottomColor:'gray' }}>
                    <Text
                      style={{ color: Colors.themeColor,fontWeight:'bold',width:"45%",marginLeft:"8%"}}
                    >
                      Total:
                    </Text>
                    <Text style={{ color: Colors.themeColor, fontWeight:'bold',width:"16%",textAlign:"center" }}>
                      {cartTotalPackages}
                    </Text>
                    {cartTotalAmount==0?<Text style={{ color: Colors.textGreyColor,width:"21%",textAlign:"right" }}>
                    £ {cartTotalAmount}
            
                    </Text>:<Text style={{ color: Colors.textGreyColor,width:"27%",textAlign:"right" }}>
                    £ {parseFloat(cartTotalAmount).toFixed(2)}
            
                    </Text>}
                    
                  </View>
                    </View>

                    
                  </View>

                  
                </View>
                
              </View>

              
             
            </Card>
          </View>
          <View style={{ height: "4%", bottom: 40, }}>
            <View style={{ padding: 0 }}>
              <Card style={{ elevation: 0 }}>
                <TextInput
                  style={styles.note_inputArea}
                  placeholder="Write any Notes"
                  autoCapitalize="none"
                  placeholderTextColor="black"
                  value={note}
                  required={true}
                  onChangeText={(value) => setNote(value)}
                  initialValue=""
                />
              </Card>
            </View>

            <TouchableOpacity
              style={styles.signupButton}
              activeOpacity={0.7}
              disabled={sendButtonCheck}
              onPress={sendOrder}
            >
              {loading ? (
                <Spinner color={"white"} />
              ) : (
                <Text style={styles.signupButtonText}>SEND ORDER</Text>
              )}
            </TouchableOpacity>
          </View>
        </View>
      </ScrollView>
      </KeyboardAvoidingView>
    </View>
    </>
  );
}

const styles = StyleSheet.create({
  signupButtonText: {
    fontSize: 20,
    color: "#ffffff",
    fontWeight: "bold",
    textAlign: "center",
    

    //marginTop: 5,
  },
  AddButtonText: {
    fontSize: 15,
    color: "#ffffff",
    fontWeight: "bold",
    textAlign: "center",

    //marginTop: 5,
  },

  signupText: {
    fontSize: 14,
    fontWeight: "bold",
    // color:'rgba(255,255,255, 0.7)',
    color: "black",
  },

  signupButton: {
    marginTop: 10,
    marginBottom: 70,
    height: 40,
    width: 300,
    backgroundColor: Colors.themeColor,
    alignSelf: "center",
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 25,
    // marginVertical: 20,
  },
  AddButton: {
    // marginTop: 10,
    marginBottom:Platform.OS=="android"?0 :0,
    height: 30,
    width: 40,
    backgroundColor: Colors.themeColor,
    alignSelf: "center",
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 5,
    // marginVertical: 20,
  },

  inputArea: {
    alignSelf: "center",
    marginVertical: 10,
    height: 40,
    width: 320,
    backgroundColor: "#F2F1F3",
    borderRadius: 25,
    paddingHorizontal: 30,
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
  auto_inputArea: {
    alignSelf: "center",
    marginVertical: 10,
    height: 40,
    // width:320,
    //  backgroundColor: '#F2F1F3',
    //borderRadius:25,
    paddingHorizontal: 30,
  },
  o_inputArea: {
    alignSelf: "center",
    //   marginVertical:10,
    color: "black",
    fontSize: 15,
    padding: 6,
    borderColor: Colors.textGreyColor,
    borderWidth: 1,
    backgroundColor:'#F2F2F2',
    // paddingBottom:12.5,
    // fontSize:14,
    height: Platform.OS=="android"?44:39,
    width: "100%",
    // width:40,
    //    backgroundColor: '#F2F1F3',
    //  marginLeft:3
    //borderRadius:25,
    //paddingHorizontal:30,
  },
  q_inputArea: {
    alignSelf: "center",
    // marginVertical:10,
    height: 10,
    width: 40,
    backgroundColor: "#F2F1F3",
    //   borderRadius:25,
    //   paddingHorizontal:30,
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
  verticleLine: {
    // marginRight:30,
    marginTop: 20,

    height: 1,
    width: "100%",
    backgroundColor: Colors.textGreyColor,
  },
  container: {
    backgroundColor: "#F5FCFF",
    // flex: 1,
    padding: 16,
    // marginTop: 40,
  },
  autocompleteContainer: {
    flex: 1,
    left: 0,
    // position: 'absolute',

    right: 0,
    top: 0,
    zIndex: 1,
  },
  descriptionContainer: {
    flex: 1,
    justifyContent: "center",
  },
  itemText: {
    fontSize: 12,
    paddingTop: 5,
    paddingBottom: 5,
    margin: 2,
  },
  infoText: {
    textAlign: "center",
    fontSize: 16,
  },
  container: {
    flex: 1,
  },
  viewHolder: {
    height: 55,
    backgroundColor: "#ff4081",
    justifyContent: "center",
    alignItems: "center",
    margin: 4,
  },
  headerText: {
    color: "white",
    fontSize: 25,
  },
  buttonDesign: {
    position: "absolute",
    right: 25,
    bottom: 25,
    borderRadius: 30,
    width: 60,
    height: 60,
    justifyContent: "center",
    alignItems: "center",
  },
  buttonImage: {
    resizeMode: "contain",
    width: "100%",
  },
  bottomNavigationView: {
    backgroundColor: "#F2F1F3",
    width: "100%",
    height: "100%",

    // justifyContent: 'center',
    //alignItems: 'center',
  },
  inputContainer: {
    minWidth: 300,
    width: "90%",
    height: 55,
    backgroundColor: "transparent",
    color: "#6C6363",
    fontSize: 18,
    fontFamily: "Roboto",
    borderBottomWidth: 1,
    borderBottomColor: "rgba(108, 99, 99, .7)",
  },
  uploadButton: {
    height: 40,
    width: 300,
    borderWidth: 2,
    flexDirection: "row",
    borderColor: "white",
    backgroundColor: Colors.themeColor,
    alignSelf: "center",
    borderRadius: 25,
  },
  uploadButtonText: {
    fontSize: 20,
    marginTop: 5,
    color: "white",
    fontWeight: "bold",
    justifyContent: "center",
    marginLeft: "20%",
  },
  centeredView2: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    // marginTop: 60,
    

  },
  modalView2: {
    margin: 20,
    // height:"100%",
    height:'100%',
    width:"100%",
    backgroundColor: 'rgba(0,0,0,0.3)',
   // borderRadius: 20,
    // padding: 35,
    alignItems: "center",
    justifyContent:'center',
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2
    },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5
  },
  signupButtonText1:{
    fontSize: 20,
  color: "white",
  fontWeight: '700',
  textAlign: 'center',
  },
  bu_signupButtonText1:{
      fontSize: 20,
    color: Colors.themeColor,
    fontWeight: 'bold',
    textAlign: 'center',
    },
    signupButton1: {
      marginTop:5,
    height: 30,
  width: 150,
backgroundColor: Colors.themeColor,
justifyContent:"center",
alignSelf:'center',
borderRadius: 25,
// marginVertical: 20,
  },
  bu_signupButton1: {
    marginTop:10,
  height: 30,
width: 150,
backgroundColor: 'white',
borderColor:Colors.themeColor,
borderWidth:2,
justifyContent:"center",
alignSelf:'center',
borderRadius: 25,
// marginVertical: 20,
},



});

const mapStateToProps = (state) => {
  return {
    cardItemsArray: state,
    // selectedMeal : state
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    removeItem: (product) =>
      dispatch({ type: "REMOVE_FROM_CART", product: product }),
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(CreateNewOrder);

