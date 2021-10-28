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
import URL from "../../src/api/ApiURL";
import * as ApiDataAction from "../../src/store/actions/ApiData";
// import Toast from "react-native-simple-toast";

import { useSelector, useDispatch } from "react-redux";
// import { color } from "react-native-reanimated";

const ForgotPasswordVerification = ({ navigation }) => {
  const dispatch = useDispatch();

  const [email, setEmail] = useState("");
  const [newEmail, setNewEmail] = useState("");
  const [loading, setLoading] = useState(false);

  const [password, setPassword] = useState("");

  const search_Email = () => {
    //console.log("ph o", email);
    if (email != "") {
      setLoading(true);

      fetch(URL + "/get_email_phone/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          username: email,
          user_type: "client",
        }),
      })
        .then(async (response) => {
          let data = await response.json();
          console.log("signup", data);

          console.log("signup", response.status);
          if (response.status == 200) {
            setNewEmail(data.data.email);
            setPassword(data.data.phone);
            setLoading(false);
            dispatch(ApiDataAction.SetEmail(email));

            navigation.navigate("ForgotPassword", {
              email: email,
              phone: data.data.phone,
            });
            setEmail("");
          } else {
            setLoading(false);
            alert(data.message);
            // Toast.show(data.message, Toast.LONG);

            //alert(data.message);

            //  alert(data.message);
          }
          //send_Verification_Code()
          // navigation.navigate("Ver

          //setResponse(json);
        })
        .catch((error) => console.log(error));
    } else {
      alert("Please enter your email")
      // Toast.show("Please Enter Your Email", Toast.LONG);
    }
  };

  return (
    <View style={{ flex: 1, height: "100%" }}>
      <View style={{ height: "30%" }}>
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
            RESET
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
      </View>

      
      <View style={styles.inputArea}>
        <TextInput
          style={{ width: 250 }}
          placeholder="Enter Your Email"
          autoCapitalize="none"
          required={true}
          placeholderTextColor={Colors.productGrey}
          minLength={6}
          errorMessage="Please enter Minimum 6 characters password"
          value={email}
          onChangeText={(value) => setEmail(value)}
          initialValue=""
        />
      </View>

      <TouchableOpacity onPress={search_Email} style={styles.button}>
        {loading ? (
          <Spinner color={"white"} />
        ) : (
          <Text
            style={{
              color: "white",
              fontWeight: "bold",
              textAlign: "center",
              fontSize: 16,
            }}
          >
            NEXT
          </Text>
        )}
      </TouchableOpacity>
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
  inputArea: {
    marginVertical: 5,
    alignSelf: "center",

    height: 40,
    width: "85%",
    backgroundColor: "#E2E2E2",
    borderRadius: 25,
    paddingHorizontal: 30,
    flexDirection: "row",
    marginTop: 80,
  },
});

export default ForgotPasswordVerification;
