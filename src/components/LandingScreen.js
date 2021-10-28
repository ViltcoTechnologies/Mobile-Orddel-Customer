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

const LandingScreen = ({ navigation }) => {
  return (
    <ImageBackground
      source={require("../assets/landingScreen.jpg")}
      style={{ justifyContent: "flex-end", flex: 1, paddingBottom: 100 }}
    >
      <TouchableOpacity
        style={styles.button}
        onPress={() => {
          navigation.navigate("FirstView");
        }}
      >
        {/* <Text style={styles.buttonText}>And Kindly click on verification link we have sent on your email</Text> */}
        <Text style={styles.buttonText}>OK</Text>
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
    marginTop: 500,
    // marginLeft:10
    //marginVertical: 20,
  },

  buttonText: {
    fontSize: 20,
    color: Colors.darkRedColor,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 5,
  },
});

export default LandingScreen;
