import React from "react";
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
} from "native-base";
import {
  StyleSheet,
  View,
  ImageBackground,
  Image,
  Linking,
  TouchableOpacity,
} from "react-native";
import Colors from "../ColorCodes/Colors";
// import { Icon } from 'react-native-elements'

const EmailVerification = ({ navigation }) => {
  return (
    <ImageBackground
      source={require("../assets/email.jpg")}
      style={{ flex: 1, justifyContent: "flex-end", paddingBottom: 100 }}
    >
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("LandingScreen")}
      >
        <Text style={styles.buttonText}>CONTINUE</Text>
      </TouchableOpacity>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  button: {
    height: 40,
    width: 300,
    backgroundColor: "white",
    justifyContent: "flex-end",
    alignSelf: "center",
    borderRadius: 25,

    // marginLeft:10
    //marginVertical: 20,
  },

  buttonText: {
    fontSize: 20,
    color: Colors.darkRedColor,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 7,
  },
});

export default EmailVerification;
