import React, { useState, useEffect } from "react";
import {
  CommonActions,
  NavigationContainer,
  useRoute,
} from "@react-navigation/native";
import {
  createStackNavigator,
  HeaderBackButton,
} from "@react-navigation/stack";
import {
  SafeAreaView,
  StyleSheet,
  StatusBar,
  NativeModules,
  processColor,
  Image,
  View,
  TouchableOpacity
} from "react-native";
import * as cartActions from "../store/actions/OrderBox";
import { useSelector, useDispatch } from "react-redux";
import Feather from "react-native-vector-icons/Feather";

import Colors from "../ColorCodes/Colors";
import { Component } from "react";
import "react-native-gesture-handler";
import { createDrawerNavigator } from "@react-navigation/drawer";
import DrawerContent from "./Drawer/DrawerContent";
import FirstView from "../FirstView";
import Login from "../components/Login";
import Signup from "../components/Signup";
import Dashboard from "../components/dashboard/Dashboard";
import VerificationCode from "../components/verification/VerificationCode";
import CreateNewOrder from "../components/CreateNewOrder";
import LandingScreen from "../components/LandingScreen";
import ShippmentAddresses from "../components/ShippmentAddresses/ShippmentAddresses";
// import BankDetail from "../components/BankDetails/BankDetail";
import BuisnessDetail from "../components/BuisnessDetails/BuisnessDetail";
import NewShippmentAddress from "../components/ShippmentAddresses/NewShippmentAddress";
import NewBankDetail from "../components/BankDetails/NewBankDetail";
import NewBuisnessDetail from "../components/BuisnessDetails/NewBuisnessDetail";
import EmailVerification from "../components/EmailVerification";
import CompletedOrdersList from "../components/CompletedOrderList";
import InProgressListOrders from "../components/InProgressOrdersList";
import AsyncStorage from "@react-native-community/async-storage";
import OrderStatus from "../components/OrdersStatus";
import PendingOrders from "../components/PendingOrders";
import OrderCartItem from "../components/OrderCardItem";
import Profile from "../components/Profile";
import Support from "../components/Support";
import ForgotPassword from "../components/ForgotPassword";
import CompletedOrderInvoice from "../components/CompletedOrderInvoice";
import InvoiceItem from "../components/InvoiceItem";
import ForgotPasswordVerification from "../components/ForgotPasswordVerification";
import ChangeForgotPassword from "../components/ChangeForgotPassword";
import ChangePasswordByEmail from "../components/ChangePasswordByEmail";
import EditBuisnessDetail from "../components/BuisnessDetails/EditBuisnessDetail";
import RejectedOrders from "../components/RejectedOrders";
import Packages from "../components/Packages";
import RejectedOrdersStatus from "../components/RejectedOrderStatus";
import PaymentMethods from "../components/PaymentMethods"
import TermCondition from '../components/TermsConditions';
import ReOrder from '../components/ReOrder';
const Stack = createStackNavigator();
function MyStack() {
  const dispatch=useDispatch();
  const [checkLogin, setCheckLogin] = useState(false);

  var getToken = async () => {
    console.log("Hi Shaheer Welcome to Hell");

    try {
      let check = await AsyncStorage.getItem("loginCheck");
      let datae = JSON.parse(check);
      setCheckLogin(datae);
      console.log(datae, "from my stack -------------------------");
      // let datap = JSON.parse(userPass);
      // setPassword(datap)

      //console.log(datae , datap);
      // if(datae != null && datap != null){

      // loadData()
      // }
    } catch (error) {
      console.log("Something went wrong", error);
    }
  };

  useEffect(() => {
    // getToken();
  }, []);

  const Drawer = createDrawerNavigator();

  function MyDrawer({ route, navigation }) {
    //const {Company_Data} = route.params

    return (
      //  <>
      // <SafeAreaView style={styles.topSafeArea} />
      // <SafeAreaView style={styles.bottomSafeArea}>
      // <StatusBar barStyle="default" backgroundColor="#0f70b7" />
      <Drawer.Navigator
        drawerContent={(props) => <DrawerContent {...props} />}
        drawerStyle={{ width: 280 }}
      >
        <Drawer.Screen
          name="Dashboard"
          component={Dashboard}
          options={{
            headerShown: true,
            title: "DASHBOARD",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        {/* <Drawer.Screen name="CreateNewOrder" component={CreateNewOrder} /> */}
        {/* <Drawer.Screen name="BuisnessDetail" component={BuisnessDetail} /> */}
        {/* <Drawer.Screen
          name="PendingOrders"
          component={PendingOrders}
          options={{ headerShown: false }}
        /> */}
        <Drawer.Screen
          name="ChangeForgotPassword"
          component={ChangeForgotPassword}
          options={{ headerShown: false,
          //   header: ({ goBack }) => ({
          //     left: ( <Icon name={'chevron-left'} onPress={ () => { goBack() } }  /> ),
          // }),
          // headerBackTitleVisible: false
          }}
        />
        <Drawer.Screen
          name="ChangePasswordByEmail"
          component={ChangePasswordByEmail}
          options={{ headerShown: false ,
            headerBackTitleVisible: false}}
        />
        {/* <Drawer.Screen
          name="EditBuisnessDetail"
          component={EditBuisnessDetail}
          options={{ headerShown: false }}
        /> */}
        {/* <Drawer.Screen
          name="RejectedOrders"
          component={RejectedOrders}
          options={{ headerShown: false }}
        /> */}
        {/* <Drawer.Screen
          name="RejectedOrdersStatus"
          component={RejectedOrdersStatus}
          options={{ headerShown: false }}
        /> */}

        {/* <Drawer.Screen name="Profile" component={Profile} /> */}
        <Drawer.Screen
          name="OrderCartItem"
          component={OrderCartItem}
          options={{ headerShown: false }}
        />
        {/* <Drawer.Screen
          name="Support"
          component={Support}
          options={{ headerShown: false }}
        /> */}
        <Drawer.Screen
          name="ForgotPassword"
          component={ForgotPassword}
          options={{ headerShown: false,
            headerBackTitleVisible: false }}
        />
        <Drawer.Screen
          name="ForgotPasswordVerification"
          component={ForgotPasswordVerification}
          options={{ headerShown: false,
            headerBackTitleVisible: false }}
        />
        {/* <Drawer.Screen
          name="CompletedOrderInvoice"
          component={CompletedOrderInvoice}
          options={{ headerShown: false }}
        /> */}
        <Drawer.Screen
          name="InvoiceItem"
          component={InvoiceItem}
          options={{ headerShown: false }}
        />

        <Drawer.Screen
          name="ShippmentAddresses"
          component={ShippmentAddresses}
        />

{/* <Drawer.Screen
          name="Packages"
          component={Packages}
          options={{
            headerShown: true,
            title: "PACKAGES",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        /> */}
        {/* <Drawer.Screen name="BankDetail" component={BankDetail} /> */}
        {/* <Drawer.Screen
          name="CompletedOrdersList"
          component={CompletedOrdersList}
          options={{ headerShown: false }}
        /> */}
        {/* <Drawer.Screen
          name="InProgressListOrders"
          component={InProgressListOrders}
          options={{ headerShown: false }}
        /> */}
        {/* <Drawer.Screen name="OrderStatus" component={OrderStatus} /> */}
        {/* <Drawer.Screen name="BuisnessDetail" component={BuisnessDetail}  options={{headerShown: false}}/> */}
      </Drawer.Navigator>

      //  </SafeAreaView>
      //   </>
    );
  }

  return (
    <NavigationContainer>
      <Stack.Navigator>
        {/* {this.LoginCheck? */}
        {/* <Stack.Screen name="Dashboard" component={Dashboard} options={{headerShown: false}}/> */}
        <Stack.Screen
          name="FirstView"
          component={FirstView}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Login"
          component={Login}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Signup"
          component={Signup}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Profile"
          component={Profile}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "PROFILE",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        {/* } */}

        {/* <Stack.Screen name="Dashboard" component={Dashboard} options={{headerShown: false}}/> */}
        <Stack.Screen
          name="ForgotPasswordVerification"
          component={ForgotPasswordVerification}
          options={{
            headerShown: true,
            title: "RESET PASSWORD",
            headerBackTitleVisible: false,
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="VerificationCode"
          component={VerificationCode}
          options={{ headerShown: false,
            headerBackTitleVisible: false }}
        />
        <Stack.Screen
          name="ChangePasswordByEmail"
          component={ChangePasswordByEmail}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "CHANGE PASSWORD",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="ChangeForgotPassword"
          component={ChangeForgotPassword}
          options={{
            headerShown: true,
            title: "CHANGE PASSWORD",
            headerBackTitleVisible: false,
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="EditBuisnessDetail"
          component={EditBuisnessDetail}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "EDIT DETAILS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />

<Stack.Screen name="Packages" component={Packages} options={{
     headerShown: true,
     title:"PACKAGES",
     headerTitleStyle:{
       color:"white",
       alignSelf:'center'
     },
     headerBackTitleVisible: false,
     headerStyle:{
      backgroundColor:Colors.themeColor,
    },
    headerTintColor: '#ffffff',
    headerRight: ()=><Image source={require('../assets/colorLogo.png')} style={{width:Platform.OS=='ios'? 40:50,height:Platform.OS=='ios'? 40:50}} />

   }}/>
        <Stack.Screen
          name="EmailVerification"
          component={EmailVerification}
          options={{ headerShown: false ,
            headerBackTitleVisible: false,}}
        />
        <Stack.Screen
          name="LandingScreen"
          component={LandingScreen}
          options={{ headerShown: false ,
            headerBackTitleVisible: false,}}
        />
        <Stack.Screen
          name="CreateNewOrder"
          component={CreateNewOrder}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "CREATE NEW ORDER",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="InvoiceItem"
          component={InvoiceItem}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="BuisnessDetail"
          component={BuisnessDetail}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "BUSINESS DETAILS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="CompletedOrderInvoice"
          component={CompletedOrderInvoice}
          options={{
            headerShown: true,
            title: "INVOICE",
            headerBackTitleVisible: false,
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="NewBuisnessDetail"
          component={NewBuisnessDetail}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "ADD DETAILS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="InProgressListOrders"
          component={InProgressListOrders}
          options={{
            headerShown: true,
            //headerTitle:false,
            //headerLeftTitle: false,
            headerBackTitleVisible: false,
            title: "IN PROGRESS ORDERS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
            // headerLeft: ()=>
            //   ({

            //     labelVisible={false}
            //   })

          //   header: () => ({
          //     left: (  onPress={  goBack()  }   ),
          // }),

          }}
        />
        <Stack.Screen name="TermCondition" component={TermCondition}
   options={{
     headerShown: true,
     title:"TERMS & CONDITIONS",
     headerTitleStyle:{
       color:"white",
       alignSelf:'center'
     },
     headerBackTitleVisible: false,
     headerStyle:{
      backgroundColor:Colors.themeColor,
    },
    headerTintColor: '#ffffff',
    headerRight:
      // <View style={{height:'100%',width:'20%',justifyContent:'center'}}>
        ()=><Image source={require('../assets/colorLogo.png')} style={{width:Platform.OS=='ios'? 40:50,height:Platform.OS=='ios'? 40:50}} />

        // </View>

   }}/>
        <Stack.Screen
          name="ForgotPassword"
          component={ForgotPassword}
          options={{
            headerShown: true,
            title: "RESET PASSWORD",
            headerBackTitleVisible: false,
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />

        <Stack.Screen
          name="PendingOrders"
          component={PendingOrders}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "NEW ORDERS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />

        <Stack.Screen
          name="ShippmentAddresses"
          component={ShippmentAddresses}
          options={{ headerShown: false ,
            headerBackTitleVisible: false,}}
        />
        <Stack.Screen
          name="RejectedOrders"
          component={RejectedOrders}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "REJECTED ORDERS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="RejectedOrdersStatus"
          component={RejectedOrdersStatus}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "REORDER",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="ReOrder"
          component={ReOrder}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "REORDER",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="CompletedOrdersList"
          component={CompletedOrdersList}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "COMPLETED ORDERS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="OrderStatus"
          component={OrderStatus}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "ORDER STATUS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="OrderCartItem"
          component={OrderCartItem}
          options={{ headerShown: false ,
            headerBackTitleVisible: false,}}
        />

        <Stack.Screen
          name="NewShippmentAddress"
          component={NewShippmentAddress}
          options={{ headerShown: false,
            headerBackTitleVisible: false, }}
        />
        {/* <Stack.Screen
          name="BankDetail"
          component={BankDetail}
          options={{
            headerShown: true,
            title: "BANK DETAILS",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        /> */}

<Stack.Screen
          name="PaymentMethods"
          component={PaymentMethods}
          options={{
            headerShown: true,
            title: "PAYMENT",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerBackTitleVisible: false,
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="Support"
          component={Support}
          options={{
            headerShown: true,
            headerBackTitleVisible: false,
            title: "SUPPORT",
            headerTitleStyle: {
              color: "white",
              alignSelf: "center",
            },
            headerStyle: {
              backgroundColor: Colors.themeColor,
            },
            headerTintColor: "#ffffff",
            headerRight: () => (
              <Image
                source={require("../assets/colorLogo.png")}
                style={{
                  width: Platform.OS == "ios" ? 40 : 50,
                  height: Platform.OS == "ios" ? 40 : 50,
                }}
              />
            ),
          }}
        />
        <Stack.Screen
          name="NewBankDetail"
          component={NewBankDetail}
          options={{ headerShown: false ,
            headerBackTitleVisible: false,}}
        />
        <Stack.Screen
          name="MyDrawer"
          component={MyDrawer}
          options={{ headerShown: false ,
            headerBackTitleVisible: false,}}
        />


      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default MyStack;
// const Stack = createStackNavigator();
// const Drawer = createDrawerNavigator();

// const Mystack=()=>{
// constructor(props){
//   super(props);
//   this.state = {
//     DrawerData: [],
//     LoginCheck:false
//   }

// }
// componentDidMount() {

//       let loginCheck =AsyncStorage.getItem("loginCheck");
//      this.LoginCheck=loginCheck;
// }

// render(){

//   const { route } = this.props;

// function Logout({ navigation }) {
//   return (
//     <>
// <SafeAreaView style={styles.topSafeArea} />
// <SafeAreaView style={styles.bottomSafeArea}>
// <StatusBar barStyle="default" backgroundColor="#0f70b7" />
// <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
//   <Button onPress={() => navigation.navigate("Login")} title="Logout" />
// </View>
//   </SafeAreaView>
// </>
// );
// }

// function MyDrawer({route,navigation}) {

//const {Company_Data} = route.params

//  return (
//   //  <>
//   // <SafeAreaView style={styles.topSafeArea} />
//   // <SafeAreaView style={styles.bottomSafeArea}>
//   // <StatusBar barStyle="default" backgroundColor="#0f70b7" />
//    <Drawer.Navigator  drawerContent = {props =>  <DrawerContent {...props}  />}  drawerStyle={{width: 280}}>

//   <Drawer.Screen name="Dashboard" component={Dashboard}/>
//   <Drawer.Screen name="CreateNewOrder" component={CreateNewOrder} />
//   <Drawer.Screen name="BuisnessDetail" component={BuisnessDetail} />
//   <Drawer.Screen name="ShippmentAddresses" component={ShippmentAddresses} />
//         <Drawer.Screen name="BankDetail" component={BankDetail} />

//    </Drawer.Navigator>

//  </SafeAreaView>
//   </>
//    );
//  }
//     return (
//   <>
// <SafeAreaView style={styles.topSafeArea} />
// <SafeAreaView style={styles.bottomSafeArea}>
//       <NavigationContainer>
//       <Stack.Navigator>

//      {/* {this.LoginCheck? */}
//      {/* <Stack.Screen name="Dashboard" component={Dashboard} options={{headerShown: false}}/> */}
//      <Stack.Screen name="FirstView" component={FirstView} options={{headerShown: false}}/>,
//  <Stack.Screen name="Login" component={Login} options={{headerShown: false}}/>,
//  <Stack.Screen name="Signup" component={Signup} options={{headerShown: false}}/>
//      {/* } */}

//  {/* <Stack.Screen name="Dashboard" component={Dashboard} options={{headerShown: false}}/> */}
//  <Stack.Screen name="VerificationCode" component={VerificationCode}
//  options={{headerShown: false}}/>
//  <Stack.Screen name="EmailVerification" component={EmailVerification} options={{headerShown: false}}/>
//  <Stack.Screen name="LandingScreen" component={LandingScreen} options={{headerShown: false}}/>
//  <Stack.Screen name="CreateNewOrder" component={CreateNewOrder}
//  options={{headerShown: false}}/>
//  <Stack.Screen name="BuisnessDetail" component={BuisnessDetail}  options={{headerShown: false}}/>
//  <Stack.Screen name="NewBuisnessDetail" component={NewBuisnessDetail}
//  options={{headerShown: false}} />
//  <Stack.Screen name="ShippmentAddresses" component={ShippmentAddresses} options={{headerShown: false}}/>
//  <Stack.Screen name="NewShippmentAddress" component={NewShippmentAddress} options={{headerShown: false}}/>
//  <Stack.Screen name="BankDetail" component={BankDetail} options={{headerShown: false}}/>
//  <Stack.Screen name="NewBankDetail" component={NewBankDetail} options={{headerShown: false}}/>

//     <Stack.Screen name="MyDrawer" component={MyDrawer} options={{headerShown: false}}/>

//     </Stack.Navigator>

//     </NavigationContainer>
//   </SafeAreaView>
//   </>
//     );
// };
// export default Mystack;
const styles = StyleSheet.create({
  topSafeArea: {
    flex: 0,
    // backgroundColor: 'blue'
  },
  bottomSafeArea: {
    flex: 1,
    // backgroundColor: 'red'
  },
});
