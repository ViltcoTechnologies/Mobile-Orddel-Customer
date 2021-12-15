/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React, { Suspense, useEffect, useState } from "react";
import {
  Container,
  Header,
  Content,
  Input,
  Item,
  Form,
  Label,
  Button,
  Text,
  Icon,
} from "native-base";
import {
  StyleSheet,
  View,
  ImageBackground,
  Image,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  BackHandler,
} from "react-native";
import styles from "./FirstView.style";
import AsyncStorage from "@react-native-community/async-storage";
import { useSelector, useDispatch } from "react-redux";
import * as ApiDataActions from "../src/store/actions/ApiData";
import URL from "./api/ApiURL";
import Colors from "../src/ColorCodes/Colors";
const FirstView = ({ navigation }) => {
  const dispatch = useDispatch();

  const [toastMessage, setToastMessage] = useState("");
  const [loading, setLoading] = useState(false);
  var getToken = async () => {
    //console.log("Hi Shaheer Welcome to Hell");

    try {
      let check = await AsyncStorage.getItem("loginCheck");
      let remember = await AsyncStorage.getItem("remember");
      let dataR = JSON.parse(remember);
      let datal = JSON.parse(check);
      // setCheckLogin(datal);

      let userEmail = await AsyncStorage.getItem("userData");

      let userPass = await AsyncStorage.getItem("passData");

      let datae = JSON.parse(userEmail);

      // setEmail(datae);
      // console.log(email)

      let datap = JSON.parse(userPass);
      if (datal && dataR) {
        setLoading(true);

        fetch(URL + "/client_app/client_login/", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: datae,
            password: datap,
          }),
        })
          .then(async (response) => {
            let data = await response.json();
            console.log("Response", data.message);

            console.log("status code", response.status);
            console.log("status code", data);
            if (data.message != "The account is not verified via email") {
              if (response.status == 200) {
                dispatch(ApiDataActions.SetLoginData(data));
                // storeToken(email, password);
                setLoading(false);
                navigation.navigate("MyDrawer");
              } else if (
                response.message == "The account is not verified via email"
              ) {
                setLoading(false);
                // alert(response.message);
              } else {
                setLoading(false);
                alert("There was a issue in your build, re-Install your app");
              }
              // code that can access both here
            } else {
              setLoading(false);

              // alert(data.message);
            }
          })
          .catch((error) => console.log("Something went wrong", error));
      }



    } catch (error) {
      console.log("Something went wrong", error);
    }
  };

  useEffect(() => {
    getToken();

    fetch(URL + "/version_control/?apk_version=1.3")
      // fetch(URL+'/client_app/clients_list/33/')
      .then(async (response) => {
        let data = await response.json();
        console.log("Show Card", data);
        console.log("Show Card Code", response.status);
        if (response.status == 200) {
          // dispatch(ApiDataAction.SetCard(data.card.card_brand,data.card.last4));
        } else {
          setLoading(false);
          Alert.alert("Hold on!", data.message, [
            {
              // text: "Cancel",
              // onPress: () => null,
              // style: "cancel"
            },
            { text: "Ok", onPress: () => BackHandler.exitApp() },
          ]);
        }
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <View style={{ flex: 1 }}>
      {/* <View style={{flex:10}} > */}
      {loading ? (
        <View
          style={{
            flex: 1,
            justifyContent: "center",
            alignItems: "center",
            alignSelf: "center",
          }}
        >
          <ActivityIndicator
            size={"large"}
            style={{ width: "20%", height: "20%" }}
          />
        </View>
      ) : (
        <ImageBackground
          source={require("./assets/Splash.jpg")}
          style={styles.image}
        >
          <View style={{ alignItems: "center", borderWidth:1 }}>
            <View style={styles.topContainer}>
              <Image
                style={styles.tinyLogo}
                source={require("./assets/colorLogo.png")}
              />
              <View
                style={{
                  //  borderColor:'white',
                  // borderWidth:1,
                  //width: "100%",
                }}
              >
                <Text
                  style={{
                    // borderColor:'white',
                    // borderWidth:1,
                    //marginLeft: "7%",
                    width: "100%",
                    // padding:20,
                    color: "white",
                    fontSize: 20,
                    fontWeight: "700",
                    textAlign: "center",
                    letterSpacing: 2,
                  }}
                >
                  Customer App
                </Text>
              </View>
            </View>

            {/* </View> */}

            {/* <View style = {{flex:3}}> */}
            <View
              style={{
                width: "100%",
                height: "40%",
              }}
            >
              <TouchableOpacity
                onPress={() => navigation.navigate("Signup")}
                style={{
                  width: "80%",
                  borderRadius: 30,
                  backgroundColor: Colors.darkRedColor,
                }}
                style={{
                  ...styles.secondSubmitButton,
                  backgroundColor: "white",
                  borderWidth: 1,
                  borderColor: Colors.darkRedColor,
                }}
              >
                <Text
                  style={{
                    fontWeight: "bold",
                    color: Colors.darkRedColor,
                    fontSize: 16,
                    textAlign: "center",
                  }}
                >
                  Register Yourself
                </Text>
              </TouchableOpacity>

              <TouchableOpacity
                onPress={() => navigation.navigate("Login")}
                style={{
                  ...styles.secondSubmitButton,
                  backgroundColor: "white",
                  borderWidth: 1,
                  borderColor: Colors.darkRedColor,
                  marginTop: 20,
                }}
              >
                <Text
                  style={{
                    fontWeight: "bold",
                    color: Colors.darkRedColor,
                    fontSize: 16,
                    textAlign: "center",
                  }}
                >
                  Login
                </Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* </View> */}
        </ImageBackground>
      )}
    </View>
  );
};

export default FirstView;
