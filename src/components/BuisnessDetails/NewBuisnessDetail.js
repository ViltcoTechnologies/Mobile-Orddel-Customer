import React, { useState, useEffect, useRef } from "react";
import {
  Container,
  Header,
  Content,
  Input,
  Item,
  Form,
  Label,
  Button,
  Thumbnail,
  Text,
  Spinner,
  
} from "native-base";
import {
  StyleSheet,
  View,
  ImageBackground,
  KeyboardAvoidingView,
  ScrollView,
  TextInput,
  TouchableOpacity,
  Platform,
  Image,
  SafeAreaView
} from "react-native";
//import styles from './Signup.style'

// import Toast from "react-native-simple-toast";
// import PushNotificationIOS from "@react-native-community/push-notification-ios";
// import PushNotification from "react-native-push-notification";
//import PhoneInput from "react-native-phone-number-input";
import * as Animatable from "react-native-animatable";
import { useSelector, useDispatch } from "react-redux";
import * as ApiAction from "../../store/actions/ApiData";
import Colors from "../../ColorCodes/Colors";
import AntDesign from "react-native-vector-icons/AntDesign";
import URL from "../../api/ApiURL";

// import Firebase from '@react-native-firebase/app'

const NewBuisnessDetail = ({ navigation }) => {
  const ClientId = useSelector((state) => state.ApiData.ClientId);
  const ClientName = useSelector((state) => state.ApiData.ClientName);
  const ClientImage = useSelector((state) => state.ApiData.ClientImage);

  console.log("ClientId", ClientId);
  const phoneInput = useRef(phone_No);
  const [value, setValue] = useState("");
  const [formattedValue, setFormattedValue] = useState("");
  const [username, setUserName] = useState("");
  // const [email , setEmail] = useState('')
  // const [password, setPassword] = useState('')
  const [c_Pass, setC_Pass] = useState("");
  const [phone_No, setPhone_No] = useState(phoneInput);
  const [securePass, setSecurePass] = useState(true);
  const [secureConfirmPass, setSecureConfirmPass] = useState(true);

  const [BusinessName, setBusinessName] = useState("");
  const [BusinessNature, setBusinessNature] = useState("");
  const [BusinessType, setBusinessType] = useState("");
  const [address, setAddress] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const [BusinessNameMsg, setBusinessNameMsg] = useState(false);
  const [BusinessNatureMsg, setBusinessNatureMsg] = useState(false);
  const [BusinessTypeMsg, setBusinessTypeMsg] = useState(false);

  const [BusinessNameMsg1, setBusinessNameMsg1] = useState(false);
  const [BusinessNatureMsg1, setBusinessNatureMsg1] = useState(false);
  const [BusinessTypeMsg1, setBusinessTypeMsg1] = useState(false);
  var reg1=/^[a-zA-Z ]*$/;

  const [addressMsg, setAddressMsg] = useState(false);
  const [loading, setLoading] = useState(false);
  const [buttonCheck,setButtonCheck]=useState(false);
  const [tokken, setTokken] = useState("");


  const checkName=()=>{
    if(BusinessName!=""){
      if (reg1.test(BusinessName) === false) {
        // setToastMessage("Email is Not Correct");
        // alert("Invalid Business Name");
        setBusinessNameMsg1(true);
        setBusinessName("");
        // setButtonCheck(false);
        // setAccountNumberMsg1(true);
        // setLoading(false);
        return false;
      }
      else{
        setBusinessNameMsg1(false);
      }
    }
  }

  const checkNature=()=>{
    if(BusinessNature!=""){
      if (reg1.test(BusinessNature) === false) {
        // setToastMessage("Email is Not Correct");
        // alert("Invalid Business Nature");
        setBusinessNatureMsg1(true);
        setBusinessNature("");
        // setButtonCheck(false);
        // setAccountNumberMsg1(true);
        // setLoading(false);
        return false;
      }
      else{
        setBusinessNatureMsg1(false);
      }
      
    }
  }

  const checkType=()=>{
    if(BusinessType!=""){
      if (reg1.test(BusinessType) === false) {
        // setToastMessage("Email is Not Correct");
        // alert("Invalid Business Type");
        setBusinessTypeMsg1(true);
        setBusinessType("");
        // setButtonCheck(false);
        // setAccountNumberMsg1(true);
        // setLoading(false);
        return false;
      }
      else{
        setBusinessTypeMsg1(false);
      }
    }
  }



  const postDetail = () => {
    setLoading(true);
    setButtonCheck(true);
    if (BusinessName == ""||BusinessName == " ") {
      setBusinessNameMsg(true);
      setLoading(false);
      setButtonCheck(false);
    } else {
      setBusinessNameMsg(false);
      setLoading(false);
    }
    if (BusinessNature == ""||BusinessNature==" ") {
      setButtonCheck(false);
      setBusinessNatureMsg(true);
      setLoading(false);
    } else {
      setBusinessNatureMsg(false);
      setLoading(false);
    }
    if (BusinessType == ""||BusinessType==" ") {
      setButtonCheck(false);
      setBusinessTypeMsg(true);
      setLoading(false);
    } else {
      setBusinessTypeMsg(false);
      setLoading(false);
    }
    if (address == ""||address==" ") {
      setButtonCheck(false);
      setAddressMsg(true);
      setLoading(false);
    } else {
      setAddressMsg(false);
      setLoading(false);
    }
    if(BusinessType!=""){
      if (reg1.test(BusinessType) === false) {
        // setToastMessage("Email is Not Correct");
        // alert("Invalid Business Type");
        setBusinessTypeMsg1(true);
        setBusinessType("");
        // setButtonCheck(false);
        // setAccountNumberMsg1(true);
        // setLoading(false);
        return false;
      }
      else{
        setBusinessTypeMsg1(false);
      }
    }
    if(BusinessNature!=""){
      if (reg1.test(BusinessNature) === false) {
        // setToastMessage("Email is Not Correct");
        // alert("Invalid Business Nature");
        setBusinessNatureMsg1(true);
        setBusinessNature("");
        // setButtonCheck(false);
        // setAccountNumberMsg1(true);
        // setLoading(false);
        return false;
      }
      else{
        setBusinessNatureMsg1(false);
      }
      
    }

    // if(BusinessName!=""){
    //   if (reg1.test(BusinessName) === false) {
    //     // setToastMessage("Email is Not Correct");
    //     // alert("Invalid Business Name");
    //     setBusinessNameMsg1(true);
    //     setBusinessName("");
    //     // setButtonCheck(false);
    //     // setAccountNumberMsg1(true);
    //     // setLoading(false);
    //     return false;
    //   }
    //   else{
    //     setBusinessNameMsg1(false);
    //   }
    // }
    if(BusinessName==""&&BusinessNature==""&&BusinessType==""&&address==""){
      // alert("Nothing to Change");
      setLoading(false);
    }
    else if(BusinessName==" "||BusinessNature==" "||BusinessType==" "||address==" "){
      // alert("Nothing to Change");
      setLoading(false);
    }
    else{
      console.log("BusinessName",BusinessName);
      console.log("BusinessNature",BusinessNature);
      console.log("BusinessType",BusinessType);
      console.log("ClientId",ClientId);
      console.log("address",address);
      const res = fetch(URL + "/client_app/insert_business/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: BusinessName,
          nature: BusinessNature,
          type: BusinessType,
          client: ClientId,
          address: address,
        }),
      })
        .then(async (response) => {
          setLoading(true);

          let data = await response.json();
          console.log("signup", data);
          console.log("signup", response.status);
          if (response.status == 200) {
            //navigation.navigate("VerificationCode" , {Email : email , Phone_No : phoneNumber})
            setLoading(false);

            setBusinessName("");
            setBusinessNature("");
            setBusinessType("");
            setAddress("");
           
            // dropDownAlertRef.alertWithType('success', '', 'Bussiness Details are added successfully.');
            alert("Bussiness details are added successfully")
            // Toast.show("Bussiness Details are added successfully", Toast.LONG);
            setButtonCheck(false);

            // navigation.navigate("Dashboard");
          } else {
            alert(data.message);
            setLoading(false);
            // Toast.show(data.message, Toast.LONG);
            setButtonCheck(false);

            //setLoading(false);
          }
          //send_Verification_Code()
          // navigation.navigate("VerificationCode" , {Email : email , Phone_No : phoneNumber})
        })
        .catch((error) => console.log("Something went wrong", error));
      setLoading(false);

      //console.log("res",res)
    }
  };

  //Verification Code

  //  useEffect(() => {

  //   Firebase.initializeApp

  //   PushNotification.configure({
  //     // (optional) Called when Token is generated (iOS and Android)
  //     onRegister: function (token) {
  //       setTokken(token.token)

  //       console.log("TOKEN:", token);
  //     },

  //     // (required) Called when a remote is received or opened, or local notification is opened
  //     onNotification: function (notification) {
  //       console.log("NOTIFICATION:", notification);

  //       // process the notification

  //       // (required) Called when a remote is received or opened, or local notification is opened
  //       notification.finish(PushNotificationIOS.FetchResult.NoData);
  //     },

  //     // (optional) Called when Registered Action is pressed and invokeApp is false, if true onNotification will be called (Android)
  //     onAction: function (notification) {
  //       console.log("ACTION:", notification.action);
  //       console.log("NOTIFICATION:", notification);

  //       // process the action
  //     },

  //     // (optional) Called when the user fails to register for remote notifications. Typically occurs when APNS is having issues, or the device is a simulator. (iOS)
  //     onRegistrationError: function(err) {
  //       console.error(err.message, err);
  //     },

  //     // IOS ONLY (optional): default: all - Permissions to register.
  //     permissions: {
  //       alert: true,
  //       badge: true,
  //       sound: true,
  //     },

  //     // Should the initial notification be popped automatically
  //     // default: true
  //     popInitialNotification: true,

  //     /**
  //      * (optional) default: true
  //      * - Specified if permissions (ios) and token (android and ios) will requested or not,
  //      * - if not, you must call PushNotificationsHandler.requestPermissions() later
  //      * - if you are not using remote notification or do not have Firebase installed, use this:
  //      *     requestPermissions: Platform.OS === 'ios'
  //      */
  //     requestPermissions: true,
  //   });

  // try {
  //   const Login =  AsyncStorage.getItem('@login')
  //   const Password = AsyncStorage.getItem('@password')
  //   if (Login !== null) {
  //      this.props.navigation.navigate("Dashboard")
  //   }
  // } catch (e) {
  //   alert('Failed to fetch the data from storage')
  // }

  // },[]);

  return (
    <>
     <KeyboardAvoidingView style={{ flex: 1 }}
        behavior={Platform.OS == "ios" ? "padding" : null} >
    <ScrollView keyboardShouldPersistTaps="always" style={{backgroundColor:'white'}}>
    <View style={styles.container}>
      
      
      {/* <DropdownAlert ref={ref => dropDownAlertRef = ref} updateStatusBar={false} tapToCloseEnabled={true} errorColor={Colors.themeColor} successColor={Colors.themeColor} containerStyle={{width:"80%"}} /> */}

      {/* <View style={styles.spinnerv}> */}
      {/* {
  state?
  <ActivityIndicator size={100} /> :
  <Text> loading... </Text>
} */}
      {/* </View> */}

      <View style={styles.header}>
        <ImageBackground
          source={require("../../assets/Splash.jpg")}
          style={{ width: "100%", height: "100%" }}
        >
          <Content>
            <View style={{ alignItems: "center", marginTop: 20 }}>
              <Thumbnail
                scaleX={2}
                scaleY={2}
                style={{ margin: 35 }}
                source={
                  ClientImage == null
                    ? require("../../assets/profilelogo.png")
                    : { uri: ClientImage }
                }
              />
              <Text
                style={{
                  fontWeight: "bold",
                  color: "black",
                  fontSize: 16,
                  color: Colors.yellowColor,
                }}
              >
                Business Details Of{" "}
              </Text>
              <Text
                style={{
                  fontWeight: "bold",
                  color: "black",
                  fontSize: 22,
                  color: "white",
                }}
              >
                {ClientName}
              </Text>
            </View>
            {/* <View style = {{alignItems:'center'}}>
          <Text style ={{fontWeight:'bold',color:'black',padding:5}}>Khan</Text>
          </View> */}
          </Content>
        </ImageBackground>
      </View>

      <View style={styles.footer}>
        <View
          style={{
            width: "90%",
            alignSelf: "center",
          }}
        >
          {/* <ScrollView>

<KeyboardAvoidingView
  behavior={Platform.OS === "ios" ? "padding" : null}
  style={{ flex: 0 }}
> */}
              {/* <FormSignup type="SignUp"/> */}
              {/* <SafeAreaView> */}
              <TextInput
                style={styles.inputArea}
                placeholder="Name"
                autoCapitalize="words"
                placeholderTextColor={Colors.textGreyColor}
                value={BusinessName}
                maxLength={50}
                required={true}
                onChangeText={(value) => {
                  setBusinessNameMsg(false);
                  setBusinessName(value);
                }}
                initialValue=""
              />
              {BusinessNameMsg && (
                <Animatable.View animation="fadeInLeft" duration={500}>
                  <Text style={{ color: "#DC143C", marginLeft: 20 }}>
                    Please Enter Business Name
                  </Text>
                </Animatable.View>
              )}

              <TextInput
                style={styles.inputArea}
                placeholder="Nature (Shop, Restaurant, Café etc)"
                autoCapitalize="words"
                placeholderTextColor={Colors.textGreyColor}
                maxLength={50}
                value={BusinessNature}
                required={true}
                onChangeText={(value) => {
                  setBusinessNatureMsg(false);
                  setBusinessNature(value);
                  setBusinessNatureMsg1(false);
                }}
                onEndEditing={checkNature}
                initialValue=""
              />
              {BusinessNatureMsg && (
                <Animatable.View animation="fadeInLeft" duration={500}>
                  <Text style={{ color: "#DC143C", marginLeft: 20 }}>
                    Please Enter Busines Nature
                  </Text>
                </Animatable.View>
              )}
               {BusinessNatureMsg1 && (
                <Animatable.View animation="fadeInLeft" duration={500}>
                  <Text style={{ color: "#DC143C", marginLeft: 20 }}>
                   Invalid Busines Nature
                  </Text>
                </Animatable.View>
              )}


              <TextInput
                style={styles.inputArea}
                placeholder= "Type (Company, Sole Trader etc) "
                autoCapitalize="words"
                placeholderTextColor={Colors.textGreyColor}
                maxLength={50}
                value={BusinessType}
                required={true}
                onChangeText={(value) => {
                  setBusinessTypeMsg(false);
                  setBusinessType(value);
                  setBusinessTypeMsg1(false);
                }}
                onEndEditing={checkType}
                initialValue=""
              />
              {BusinessTypeMsg && (
                <Animatable.View animation="fadeInLeft" duration={500}>
                  <Text style={{ color: "#DC143C", marginLeft: 20 }}>
                    Please Enter Business Type
                  </Text>
                </Animatable.View>
              )}
              {BusinessTypeMsg1 && (
                <Animatable.View animation="fadeInLeft" duration={500}>
                  <Text style={{ color: "#DC143C", marginLeft: 20 }}>
                    Invalid Business Type
                  </Text>
                </Animatable.View>
              )}

              <TextInput
                style={styles.inputArea}
                placeholder="Address"
                autoCapitalize="words"
                placeholderTextColor={Colors.textGreyColor}
                value={address}
                required={true}
                onChangeText={(value) => {
                  setAddressMsg(false);
                  setAddress(value);
                }}
                initialValue=""
              />
              {addressMsg && (
                <Animatable.View animation="fadeInLeft" duration={500}>
                  <Text style={{ color: "#DC143C", marginLeft: 20 }}>
                    Please Enter Address
                  </Text>
                </Animatable.View>
              )}

              {isLoading ? (
                <Spinner
                  //visibility of Overlay Loading Spinner
                  visible={isLoading}
                  // size="normal"
                  // animation='fade'
                  //Text with the Spinner
                  // textContent={'Loading...'}
                  //Text style of the Spinner Text
                  // textStyle={styles.activityIndicator}
                />
              ) : (
                <View>
                  {/* <TouchableOpacity
                    style={styles.uploadButton}
                    activeOpacity={0.7}
                  >
                    <AntDesign
                      name="upload"
                      color={Colors.themeColor}
                      size={20}
                      style={{ marginTop: 5, marginRight: 10 }}
                    />
                    <Text style={styles.uploadButtonText}>UPLOAD LOGO</Text>
                  </TouchableOpacity> */}
                  <TouchableOpacity
                  disabled={buttonCheck}
                    style={{ ...styles.signupButton, marginTop: 10 }}
                    activeOpacity={0.7}
                    onPress={postDetail}
                  >
                    {loading ? (
                      <Spinner color={"white"} />
                    ) : (
                      <Text style={styles.signupButtonText}>SUBMIT</Text>
                    )}
                  </TouchableOpacity>
                </View>
              )}
              {/* </SafeAreaView> */}
           
          {/* </KeyboardAvoidingView>
          </ScrollView> */}
          {/* {isLoading ? (
      <Spinner
      //visibility of Overlay Loading Spinner
      visible={isLoading}
      // size="normal"
      // animation='fade'
      //Text with the Spinner
      // textContent={'Loading...'}
      //Text style of the Spinner Text
      // textStyle={styles.activityIndicator}
    />):(

    // )}
    //   {isLoading ? (
    //   <ActivityIndicator size="large" color={Colors.accentColor} style={styles.activityIndicator}/>
    //   ) : ( */}
          {/* <TouchableOpacity style={styles.button}
        onPress={addCompanyInfo}
        >
        <Text style={styles.buttonText}>SIGN UP</Text>
      </TouchableOpacity> */}
          {/* //)} */}
        </View>
      </View>
     
    </View>
    </ScrollView>
    </KeyboardAvoidingView>
    </>
    
   
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#EE0202",
  },

  inputArea: {
    marginVertical: 10,
    height: 40,
    width: "100%",
    backgroundColor: "#F2F1F3",
    //  borderColor:'black',
    //  borderWidth:1,
    borderRadius: 25,
    paddingHorizontal: 30,
  },
  name_inputArea: {
    marginVertical: 10,
    height: 40,
    width: 150,
    backgroundColor: "#F2F1F3",
    borderRadius: 25,
    paddingHorizontal: 30,
  },
  name2_inputArea: {
    marginLeft: 20,
    marginVertical: 10,
    height: 40,
    width: 150,
    backgroundColor: "#F2F1F3",
    borderRadius: 25,
    paddingHorizontal: 30,
  },
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
    width: "100%",
    backgroundColor: "#EE0202",
    justifyContent: "center",
    borderRadius: 25,
    marginBottom: 20,
    // marginVertical: 20,
  },

  uploadButton: {
    height: 40,
    width: "100%",
    borderWidth: 2,
    flexDirection: "row",
    borderColor: Colors.themeColor,
    backgroundColor: "white",
    justifyContent: "center",
    borderRadius: 25,
    marginVertical: 20,
  },
  uploadButtonText: {
    fontSize: 20,
    marginTop: 5,
    color: Colors.themeColor,
    fontWeight: "bold",
    textAlign: "center",
  },

  header: {
    flex: 2,
    width: "100%",
  },

  footer: {
    flex: 3,
    width: "100%",
    backgroundColor: "#ffffff",
    // borderTopLeftRadius: 30,
    // borderTopRightRadius: 30,
    // paddingVertical: 10,
    //paddingHorizontal:Platform.OS === 'android' ?20:40
  },

  button: {
    justifyContent: "center",
    alignItems: "center",
    marginHorizontal: 10,
    //marginVertical:20,
    width: 90,
    height: 30,
    backgroundColor: "#EE0202",
    borderRadius: 25,
  },

  buttonText: {
    color: "#ffffff",
    fontWeight: "bold",
    fontSize: 20,
  },

  signupContianer: {
    flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
  },
});

export default NewBuisnessDetail;
