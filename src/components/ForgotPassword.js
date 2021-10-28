import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Platform,
  ScrollView,
  ImageBackground,
  Image,
  TextInput,
  KeyboardAvoidingView,
  SafeAreaView,
} from "react-native";
import { Spinner } from "native-base";
import Ionicons from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Colors from "../ColorCodes/Colors";
import MyHeader from "../components/MyHeader";
import { Col } from "native-base";
import URL from "../api/ApiURL";

const ForgotPassword = ({ navigation, route }) => {
  const { email, phone } = route.params;

  //console.log(email, phone);
  const [loading, setLoading] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const send_Verification_Code = () => {
    //console.log("ph o",Phone_No);

    setLoading(true);

    fetch(URL + "/send_otp/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        phone_number: phone,
      }),
    })
      .then(async (response) => {
        let data = await response.json();
        console.log("signup", response.status);

        if (response.status == 200) {
          setLoading(false);
          navigation.navigate("VerificationCode", {
            Phone_No: phone,

            EmailVerify: "ChangeForgotPassword",
          });
        } else {
          alert(data.message)
    setLoading(false);

          console.log("Verication Code Not Sent");
        }
      })
      .catch((error) => console.log(error));
  };

  const send_Email = () => {
    setIsLoading(true);
    fetch(URL + "/api/password_reset/", {
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
        console.log("signup", data);
        //setNewEmail(data.data.email);
        //setPassword(data.data.phone);
        console.log("signup", response.status);
        if (response.status == 200) {
          setIsLoading(false);
          navigation.navigate("ChangePasswordByEmail");
        } else {
          alert(data.message);

          //  alert(data.message);
        }
        //send_Verification_Code()
        // navigation.navigate("Ver

        //setResponse(json);
      })
      .catch((error) => console.log(error));
  };

  return (
    <View style={{ flex: 1, height: "100%" }}>
      {/* <View style={{ height: "20%" }}>
        <ImageBackground
          source={require("../assets/Splash.jpg")}
          style={{
            width: "100%",
            height: "100%",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Text
            style={{
              color: "white",
              fontSize: 25,
              fontWeight: "bold",
              letterSpacing: 2,
            }}
          >
            FORGOT
          </Text>
          <Text
            style={{
              color: "white",
              fontSize: 25,
              fontWeight: "bold",
              letterSpacing: 2,
            }}
          >
            PASSWORD
          </Text>
        </ImageBackground>
      </View> */}

      <View
        style={{
          height: "10%",
          width: "85%",
          alignSelf: "center",
          marginTop: 20,
          marginBottom:20
        }}
      >
        <Text
          style={{
            color: Colors.productGrey,
            fontWeight: "bold",
            textAlign: "center",
            fontSize: 16,
          }}
        >
          Select your which contact details you want
        </Text>
        <Text
          style={{
            color: Colors.productGrey,
            fontWeight: "bold",
            textAlign: "center",
            fontSize: 16,
          }}
        >
          to use for verification code
        </Text>
      </View>
      <View

        style={{
          width: "80%",
          height: 170,
          justifyContent:'center',
          alignSelf: "center",
          // alignContent:'center',
          borderRadius: 10,
          marginTop: 20,
          //borderWidth:1,
          flexDirection: "row",
          backgroundColor: "#E2E2E2",
          //justifyContent: "center",
        }}

      >
        {loading ? (
          <Spinner color={Colors.themeColor} style={{alignSelf:'center'}} />
        ) : (
          <TouchableOpacity
            onPress={send_Verification_Code}
            style={{
              width: "90%",
              height: "25%",
              alignSelf: "center",
              borderRadius: 10,
              //borderWidth:1,

              flexDirection: "row",
              backgroundColor: "#E2E2E2",
              justifyContent: "center",
            }}
          >
            <View
              style={{
                width: "15%",
                height: "100%",
               //borderWidth:1,

                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <Image
                source={require("../assets/sms.png")}
                style={{
                  width: 40,
                  height: 40,
                }}
              />
            </View>

            <View
              style={{
                width: "70%",
                height: "100%",
                paddingLeft: 20,

                justifyContent: "center",
              }}
            >
              <Text style={{ color: Colors.textGreyColor }}>Via Sms</Text>
              <Text
                style={{
                  color: Colors.productGrey,
                  fontSize: 18,
                  fontWeight: "bold",
                }}
              >
                {phone}
              </Text>
            </View>
          </TouchableOpacity>
        )}
      </View>

      <View
        style={{
          width: "80%",
          height: 170,
          justifyContent:'center',
          alignSelf: "center",
          // alignContent:'center',
          borderRadius: 10,
          marginTop: 30,
          //borderWidth:1,
          flexDirection: "row",
          backgroundColor: "#E2E2E2",
          //justifyContent: "center",
        }}
      >
        {isLoading ? (
          <Spinner color={Colors.themeColor} style={{alignSelf:'center'}} />
        ) : (
          <TouchableOpacity
            onPress={send_Email}
            style={{
              width: "80%",
              height: 80,
              alignSelf: "center",
              borderRadius: 10,
              marginTop: 20,
              //borderWidth:1,

              flexDirection: "row",
              backgroundColor: "#E2E2E2",
              // justifyContent: "center",
            }}
          >
            <View
              style={{
                width: "20%",
                //height: "100%",
                //borderWidth:1,

                justifyContent: 'flex-start',
                alignItems: "center",
              }}
            >
              <Image
                source={require("../assets/forgotemail.png")}
                style={{
                  width: 40,
                  height: 40,
                }}
              />
            </View>
            <View
              style={{
                width: "80%",
                height: "100%",
                paddingLeft: 20,
                //borderWidth:1,

                justifyContent: 'flex-start',
              }}
            >
              <Text style={{ color: Colors.textGreyColor }}>Via Email</Text>
              <Text
                style={{
                  color: Colors.productGrey,
                  fontSize: 16,
                  width: "100%",
                  fontWeight: "bold",
                  marginBottom:15
                }}
              >
                {email}
              </Text>
            </View>
          </TouchableOpacity>
        )}
      </View>

      {/* <TouchableOpacity style={styles.button}>
        <Text
          style={{
            color: "white",
            fontWeight: "bold",
            textAlign: "center",
            fontSize: 16,
          }}
        >
          SELECT PASSWORD RESET METHOD
        </Text>
      </TouchableOpacity> */}
    </View>
  );
};

const styles = StyleSheet.create({
  cartItem: {
    flex: 1,
    marginTop: 12,
    padding: 10,
    backgroundColor: "white",
    borderWidth: 0.5,
    borderColor: "#EE0202",
    flexDirection: "row",
    justifyContent: "space-between",
    marginHorizontal: 20,
    borderRadius: 15,
  },
  button: {
    height: 40,
    width: 270,
    backgroundColor: "#EE0202",
    justifyContent: "center",
    borderRadius: 25,
    marginVertical: 20,
    alignSelf: "center",
  },
});

export default ForgotPassword;
