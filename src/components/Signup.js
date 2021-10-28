import React, { useState, useEffect, useRef } from "react";
import { Spinner, Picker } from "native-base";
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
  ActivityIndicator,
  FlatList,
  Text,
  Keyboard,
  TouchableWithoutFeedback
} from "react-native";
//import styles from './Signup.style'
import Icon from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Card from "../components/Card";
import { BottomSheet } from "react-native-btr";
// import PushNotificationIOS from "@react-native-community/push-notification-ios";
// import PushNotification from "react-native-push-notification";
//import PhoneInput from "react-native-phone-number-input";
import Colors from "../ColorCodes/Colors";
import URL from "../api/ApiURL";
import PhoneInput from "react-native-phone-number-input";
import CheckBox from "@react-native-community/checkbox";
// import Firebase from '@react-native-firebase/app'


const DismissKeyboard = ({ children }) => (
  <TouchableWithoutFeedback
  onPress={() => Keyboard.dismiss()}>
   {children}
  </TouchableWithoutFeedback>
  );



const Signup = ({ navigation }) => {
  const [visible, setVisible] = useState(false);
  const toggleBottomNavigationView = () => {
    //Toggling the visibility state of the bottom sheet
    setVisible(!visible);
  };
  const [visible2, setVisible2] = useState(false);
  const toggleBottomNavigationView2 = () => {
    //Toggling the visibility state of the bottom sheet
    setVisible2(!visible2);
  };
  const phoneInput = useRef(phone_No);
  const [value, setValue] = useState("");
  const [formattedValue, setFormattedValue] = useState("");
  const [username, setUserName] = useState("");
  // const [email , setEmail] = useState('')
  // const [password, setPassword] = useState('')
  const [isEmail, setIsEmail] = useState(false);
  const [c_Pass, setC_Pass] = useState("");
  const [phone_No, setPhone_No] = useState(phoneInput);
  const [securePass, setSecurePass] = useState(true);
  const [secureConfirmPass, setSecureConfirmPass] = useState(true);
  const [loading, setLoading] = useState(false);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  // const [RiderAddress,setRiderAddress]=useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [toastMessage, setToastMessage] = useState("");
  const [riderData, setRiderData] = useState("");
  const [riderLoading, setRiderLoading] = useState(false);
  const [riderName, setRiderName] = useState("");
  const [riderAddress, setRiderAddress] = useState("");
  const [riderId, setRiderId] = useState("");
  const [selectedValue, setSelectedValue] = useState("key");
  const [terms, setTerms] = useState(false);
  const [packageData, setPackageData] = useState("");
  const [packageLoading, setPackageLoading] = useState(false);
  const rider = (name, address, id) => {
    setRiderName(name);
    setRiderAddress(address);
    setRiderId(id);
    toggleBottomNavigationView();
  };
  const [packageName, setPackageName] = useState("");
  const [packageInvoice, setPackageInvoice] = useState("");
  const [packageId, setPackageId] = useState("");
  const packagedDetail = (name, invoices, id) => {
    setPackageName(name);
    setPackageInvoice(invoices);
    setPackageId(id);
    // console.log("pid",packageId);
    toggleBottomNavigationView2();
  };

  useEffect(() => {
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

    fetch(URL + "/delivery_person/list_packages/")
      // fetch(URL+'/client_app/clients_list/33/')
      .then((response) => response.json())
      .then((responseJson) => {
        if (responseJson.all_package == "") {
          setPackageLoading(true);
        } else {
          setPackageLoading(false);
          console.log("Packages:", responseJson);
          setPackageData(responseJson.all_package);
        }

      })
      .catch((error) => console.error(error));


  }, []);

  const [tokken, setTokken] = useState("");

  const checkEmail = () => {
    let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email != "") {
      if (reg.test(email) === false) {
        setToastMessage("Email is Not Correct");

        return false;
      } else {
        fetch(URL + "/check_existing_email/", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
          }),
        })
          .then(async (response) => {
            let data = await response.json();
            console.log("Email", data);
            console.log("Email", response.status);
            if (response.status == 400) {
              // alert("works");
              setIsEmail(true);

              setToastMessage("");
            } else {
              setIsEmail(false);

              setToastMessage(data.message);
              //  setIsLoading(false);
              //  alert(data.message);
            }
          })
          .catch((error) => console.log("Something went wrong", error));
      }
    } else {
      setToastMessage("Please Enter Email");
    }
  };

  const SendOtp = () => {
    fetch(URL + "/send_otp/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        phone_number: formattedValue,
      }),
    })
      .then(async (response) => {
        let data = await response.json();
        console.log("send otp", data);
        console.log("send otp", response.status);
        if (response.status == 200) {
          setLoading(false);
          navigation.navigate("VerificationCode", {
            Email: email,
            Phone_No: formattedValue,
            EmailVerify: "EmailVerification",
            first_name: firstName,
            last_name: lastName,
            password: password,
            riderId: riderId,
            gender: "male",
            // selectedValue=="key"?"male":"female",
            packageId: "gold",
          });
          //  setEmail('');
          //  setFormattedValue('');
          //  setFirstName('');
          //  setLastName('');
          //  setPassword('');
        } else {
          setLoading(false);

          setToastMessage(data.message);
          //  setIsLoading(false);
          //  alert(data.message);
        }
      })
      .catch((error) => console.log(error));
  };

  const checkPhoneNumber = () => {
    setLoading(true);
    fetch(URL + "/check_existing_phone/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        phone: formattedValue,
      }),
    })
      .then(async (response) => {
        let data = await response.json();
        console.log("Exiting Phone Number", data);
        console.log("Exiting Phone Number", response.status);
        if (response.status == 400) {
          if (isEmail != true) {
            setLoading(false);

            alert("This email already exists, please change the email");
            setToastMessage("");
          } else {
            setToastMessage("");
            if (terms) {
              SendOtp();
            } else {
              setLoading(false);

              setToastMessage("Please accept terms & conditions");
            }
          }
        } else {
          setLoading(false);

          setToastMessage(data.message);
          //  setIsLoading(false);
          //  alert(data.message);
        }
      })
      .catch((error) => console.log("Something went wrong", error));
  };

  const addCompanyInfo = () => {
    // console.log("Phon number",formattedValue)
    let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    setToastMessage("");

    console.log("phone Number", formattedValue);
    if (
      firstName == "" &&
      lastName == "" &&
      email == "" &&
      password == "" &&
      confirmPassword == "" &&
      formattedValue == "" &&
      riderId == ""
    ) {
      alert("Please enter signup details");
    } else {
      if (email == "") {
        setToastMessage("Please enter email");
      } else {
        if (reg.test(email) === false) {
          setToastMessage("Email is not correct");

          return false;
        } else if (password != confirmPassword) {
          setToastMessage("Password doesnot match");
        } else {
          if (firstName == "") {
            setToastMessage("Please enter first name");
          } else if (lastName == "") {
            setToastMessage("Please enter last name");
          } else if (riderAddress == "") {
            setToastMessage("Please select delivery person");
          }
          // else if(packageId==""){
          //   setToastMessage("Please Select Package");
          // }
          else if (formattedValue == "") {
            setToastMessage("Please enter phone number");
          } else if (formattedValue == "") {
            setToastMessage("Please enter phone number");
          } else if (password == "") {
            setToastMessage("Please enter password");
          } else if (password.length < 8) {
            setToastMessage("Password limit should be greater than 7 digits");
          } else {
            //Password Limit

            setToastMessage("");
            if (
              firstName != "" &&
              lastName != "" &&
              email != "" &&
              password != "" &&
              confirmPassword != "" &&
              formattedValue != "" &&
              riderId != ""
            ) {
              console.log(toastMessage);
              if (
                toastMessage == "" ||
                toastMessage ==
                  "This phone number already exists as a delivery person" ||
                toastMessage == "This phone number already exists" ||
                toastMessage ==
                  "This phone number already exists as a client" ||
                toastMessage == "Please Enter Phone Number"
              ) {
                checkPhoneNumber();
                setIsLoading(true);
              }
            } else {
              setIsLoading(false);

              setToastMessage("All fields are required");
            }
          }
        }
      }
    }

    setIsLoading(false);
  };





  return (

<DismissKeyboard>

    <View style={styles.container}>
      {/* <ScrollView style={{backgroundColor:'white'}}> */}

      {/* <View style={styles.spinnerv}> */}
      {/* {
  state?
  <ActivityIndicator size={100} /> :
  <Text> loading... </Text>
      } */}

      <View style={styles.header}>
        <ImageBackground
          source={require("../assets/Splash.jpg")}
          style={{ width: "100%", height: "100%" }}
        >
          <Text
            style={{
              color: "white",
              fontSize: 35,
              alignSelf: "center",
              marginTop: "15%",
              borderBottomWidth: 1,
              borderBottomColor: "white",
              fontWeight: "bold",

            }}
          >
            SIGN UP
          </Text>
          <Text
            style={{
              color: Colors.yellowColor,
              marginVertical: 15,
              fontSize: 16,
              alignSelf: "center",
              marginTop: 10,
            }}
          >
            Enter Your Information and Register Yourself
          </Text>
        </ImageBackground>
      </View>



      <View style={styles.footer}>
        {/* <KeyboardAvoidingView
           behavior="padding"
           keyboardVerticalOffset={50}
        > */}
        <KeyboardAvoidingView
          style={{ flex: 1 }}
          behavior={Platform.OS == "ios" ? "padding" : null}
        >
          <ScrollView
            keyboardShouldPersistTaps="always"
            showsVerticalScrollIndicator={false}
          >
            {/* <FormSignup type="SignUp"/> */}
            <View style={{ flexDirection: "row", alignSelf: "center" }}>
              <TextInput
                style={styles.name_inputArea}
                placeholder="First Name"
                autoCapitalize="words"
                placeholderTextColor={Colors.textGreyColor}
                value={firstName}
                required={true}
                onChangeText={(value) => setFirstName(value)}
                initialValue=""
              />

              <TextInput
                style={styles.name2_inputArea}
                placeholder="Last Name"
                autoCapitalize="words"
                placeholderTextColor={Colors.textGreyColor}
                value={lastName}
                required={true}
                onChangeText={(value) => setLastName(value)}
                initialValue=""
              />
            </View>
            <TextInput
              style={styles.inputArea}
              placeholder="Email"
              required={true}
              autoCapitalize="none"
              placeholderTextColor={Colors.textGreyColor}
              keyboardType="email-address"
              errorMessage="Please enter a valid email address."
              value={email}
              onChangeText={(value) => {
                setToastMessage("");
                setEmail(value);
              }}
              onEndEditing={checkEmail}
              initialValue=""
            />

            <View style={styles.inputArea}>
              <TextInput
                style={{ width: "95%" }}
                placeholder="Password"
                secureTextEntry={securePass}
                autoCapitalize="none"
                required={true}
                placeholderTextColor={Colors.textGreyColor}
                minLength={6}
                errorMessage="Please enter Minimum 6 characters password"
                value={password}
                onChangeText={(value) => setPassword(value)}
                initialValue=""
              />
              <View style={{ alignSelf: "center" }}>
                <Icon
                  active
                  name={securePass ? "eye" : "eye-off"}
                  color={Colors.textGreyColor}
                  size={25}
                  onPress={() => {
                    if (securePass == true) {
                      setSecurePass(false);
                    } else {
                      setSecurePass(true);
                    }
                  }}
                />
              </View>
            </View>
            <View style={styles.inputArea}>
              <TextInput
                style={{ width: "95%" }}
                placeholder="Confirm Password"
                secureTextEntry={secureConfirmPass}
                autoCapitalize="none"
                required={true}
                placeholderTextColor={Colors.textGreyColor}
                minLength={6}
                errorMessage="Please enter minimum 6 characters password"
                value={confirmPassword}
                onChangeText={(value) => setConfirmPassword(value)}
                initialValue=""
              />
              <View style={{ alignSelf: "center" }}>
                <Icon
                  active
                  name={secureConfirmPass ? "eye" : "eye-off"}
                  color={Colors.textGreyColor}
                  size={25}
                  onPress={() => {
                    if (secureConfirmPass == true) {
                      setSecureConfirmPass(false);
                    } else {
                      setSecureConfirmPass(true);
                    }
                  }}
                />
              </View>
            </View>






              <View>
              <PhoneInput
                containerStyle={styles.phoneStyle}
                textContainerStyle={styles.textStyle}
                codeTextStyle={styles.textStyle1}
                textInputStyle={{  height: 40, justifyContent:'flex-start' , marginTop: Platform.OS == "android" ? 1 : -1,  fontSize:14,
                // fontWeight: '500'
                fontWeight: 'bold'
                }}
                ref={phoneInput}
                defaultValue={value}
               // keyboardType="decimal-pad"
                // placeholder=" Ph# without 0"
                placeholder=" Ph.No (no starting zero)"
                keyboardType="numbers-and-punctuation"
                defaultCode="GB"
                onChangeText={(text) => {
                  setValue(text);
                }}
                onChangeFormattedText={(text) => {
                  setFormattedValue(text);
                }}
                autoFocus={false}
              />
              </View>





            <View style={{ padding: 10 }}>
              <Card
                style={{
                  padding: 10,
                  borderRadius: 10,
                  backgroundColor: "#F2F1F3",
                  elevation: 0,
                  width: "90%",
                  alignSelf: "center",
                }}
              >
                <TouchableOpacity onPress={toggleBottomNavigationView}>
                  <View style={{ flexDirection: "row" }}>
                    <Text
                      style={{
                        color: Colors.themeColor,
                        fontSize: 12,
                        fontWeight: "bold",
                      }}
                    >
                      Delivery Person
                    </Text>
                    <FontAwesome
                      name="chevron-down"
                      color={Colors.themeColor}
                      size={14}
                      style={{
                        marginLeft: 5,
                        color: Colors.themeColor,
                        alignSelf: "center",
                      }}
                    />
                  </View>

                  <Text style={{ fontSize: 16, fontWeight: "bold" }}>
                    {riderName}
                  </Text>
                  <Text style={{ fontSize: 12, color: "#666666" }}>
                    {riderAddress}
                  </Text>
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
                      nestedScrollEnabled={true}
                      data={riderData}
                      style={{ padding: 10 }}
                      showsVerticalScrollIndicator={false}
                      keyExtractor={({ id }, index) => id}
                      renderItem={({ item }) => (
                        <TouchableOpacity
                          style={{
                            width: "95%",
                            marginBottom: 15,
                            alignSelf: "center",
                          }}
                          onPress={() =>
                            rider(
                              item.first_name + " " + item.last_name,
                              item.address,
                              item.id
                            )
                          }
                        >
                          <Card
                            style={{
                              borderRadius: 15,
                              padding: 10,
                            }}
                          >
                            <View
                              style={{
                                flexDirection: "column",
                              }}
                            >
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
                                    }}
                                  >
                                    {item.first_name} {item.last_name}
                                  </Text>

                                  <View
                                    style={{
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
            </View>



            <View style={{ flexDirection: "row", alignSelf: "center" }}>
              <CheckBox
                value={terms}
                onValueChange={setTerms}
                boxType="square"
                onAnimationType="fade"
                onTintColor={Colors.themeColor}
                onCheckColor={Colors.themeColor}
                tintColors={{ true: Colors.themeColor, false: "black" }}
                // style={{height:10,width:10}}
                style={{
                  transform: [
                    { scaleX: Platform.OS == "android" ? 1 : 0.7 },
                    { scaleY: Platform.OS == "android" ? 1 : 0.7 },
                  ],
                }}
              />
              <View
                style={{
                  flexDirection: "row",
                  alignSelf: "center",
                  marginBottom: Platform.OS == "android" ? null : 7,
                }}
              >
                <Text style={{ fontSize: 14, marginRight: 5 }}>Accept</Text>
                <TouchableOpacity
                  onPress={() => navigation.navigate("TermCondition")}
                >
                  <Text
                    style={{
                      fontSize: 14,
                      color: Colors.themeColor,
                      fontWeight: "bold",
                    }}
                  >
                    Terms & Conditions
                  </Text>
                </TouchableOpacity>
              </View>

              {/* <Text> {cash} </Text> */}
            </View>

            {toastMessage != "" ? (
              <Text
                style={{
                  color: Colors.themeColor,
                  fontWeight: "bold",
                  textAlign: "center",
                  marginTop: 10,
                  fontSize: 18,
                }}
              >
                {toastMessage}
              </Text>
            ) : null}
            {isLoading ? (
              <Spinner
                color={Colors.themeColor}
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
              <TouchableOpacity
                // disabled={toastMessage==""?false:true}
                style={styles.signupButton}
                activeOpacity={0.7}
                onPress={addCompanyInfo}
              >
                {loading ? (
                  <Spinner color={"white"} />
                ) : (
                  <Text style={styles.signupButtonText}> SIGN UP</Text>
                )}
              </TouchableOpacity>
            )}

            <View style={styles.signupContianer}>
              <Text style={styles.signupText}> Already have an Account! </Text>

              <TouchableOpacity onPress={() => navigation.navigate("Login")}>
                <Text
                  style={{ color: Colors.darkRedColor, fontWeight: "bold" }}
                >
                  Login
                </Text>
              </TouchableOpacity>
            </View>
          </ScrollView>
        </KeyboardAvoidingView>
        {/* </KeyboardAvoidingView> */}
      </View>
      {/* </ScrollView> */}


    </View>

</DismissKeyboard>

  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // justifyContent: 'center',
    // alignItems: 'center',
    backgroundColor: "white",
  },
  phoneStyle: {
    //borderWidth:1,
    marginVertical: 10,
    height: Platform.OS == "android" ? 50 : 60,
    width: "90%",
    backgroundColor: "#F2F1F3",
    borderRadius: 30,
    paddingHorizontal: 10,
    flexDirection: "row",
    alignSelf: "center",
  },

  textStyle: {
    borderRadius: 12,
    // paddingTop:5,
    //marginTop:10,
    textAlign:'center',
    alignContent: "center",
    backgroundColor: "#F2F1F3",
    //borderWidth:1,
    //color:'black'
    fontWeight:'bold'
  },
  inputArea: {
    marginVertical: 10,
    height: 40,
    width: "90%",
    backgroundColor: "#F2F1F3",
    borderRadius: 25,
    paddingHorizontal: 25,
    flexDirection: "row",
    alignSelf: "center",
  },
  name_inputArea: {
    marginVertical: 10,
    height: 40,
    // width:150,
    width: "42%",
    backgroundColor: "#F2F1F3",
    borderRadius: 25,
    paddingHorizontal: 25,
    // alignSelf:'center'
  },
  name2_inputArea: {
    marginLeft: 20,
    marginVertical: 10,
    height: 40,
    width: "42%",
    backgroundColor: "#F2F1F3",
    borderRadius: 25,
    paddingHorizontal: 25,
  },

  DropDown_inputArea: {
    marginVertical: 10,
    alignSelf: "center",
    height: 40,
    width: "90%",
    backgroundColor: "#F2F1F3",
    borderRadius: 25,

    paddingHorizontal: Platform.OS == "android" ? 20 : 15,
    flexDirection: "row",
  },

  signupButtonText: {
    fontSize: 20,
    color: "#ffffff",
    fontWeight: "bold",
    textAlign: "center",
  },

  signupText: {
    alignSelf: "center",
    fontSize: 14,
    // fontWeight: 'bold',
    // color:'rgba(255,255,255, 0.7)',
    color: "black",
  },

  signupButton: {
    height: 40,
    width: "50%",
    backgroundColor: "#EE0202",
    justifyContent: "center",
    alignSelf: "center",
    borderRadius: 25,
    marginVertical: 20,
  },

  header: {
    flex: 2,
    width: "100%",
    //backgroundColor:'#EE0202',
    // justifyContent: 'center',
    // alignItems: 'center',
  },

  footer: {
    flex: 6,
    width: "100%",
    // height:"100%",
    backgroundColor: "#ffffff",
    //backgroundColor: "green",
    // borderTopLeftRadius: 30,
    // borderTopRightRadius: 30,
    // paddingVertical: 10,
    // borderColor:'black',
    // borderWidth:5,
    // paddingHorizontal:Platform.OS === 'android' ?20:40
  },

  button: {
    height: 40,
    width: 300,
    backgroundColor: Colors.themeColor,
    justifyContent: "center",
    borderRadius: 25,
    marginVertical: 20,
  },

  buttonText: {
    color: "#ffffff",
    fontWeight: "bold",
    fontSize: 20,
  },

  signupContianer: {
    // flexGrow: 1,
    // justifyContent: 'center',
    alignSelf: "center",
    // alignItems: 'center',
    flexDirection: "row",
  },
  bottomNavigationView2: {
    backgroundColor: "#F2F1F3",
    width: "100%",
    height: "100%",

    // justifyContent: 'center',
    //alignItems: 'center',
  },
  textStyle1:{

    fontSize: 14,
    fontWeight:'bold',
    //borderBottomWidth:1,
   // borderBottomColor: 'black'
    //fontWeight:'500'
  }
  // g_container: {
  //   // flexGrow: 1,
  //   justifyContent: 'center',
  //   alignItems: 'center',
  //   alignSelf:'center'
  //   },
});

export default Signup;


