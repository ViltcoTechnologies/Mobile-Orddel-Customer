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
import Icon from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Colors from "../ColorCodes/Colors";
import MyHeader from "../components/MyHeader";
import { Col } from "native-base";
import URL from "../../src/api/ApiURL";
import { useSelector, useDispatch } from "react-redux";
// import Toast from "react-native-simple-toast";

const ChangeForgotPassword = ({ navigation }) => {
  const [password, setPassword] = useState("");
  const [confirmPass, setConfirmPass] = useState("");
  const [isLoading,setIsLoading]=useState(false);
  const ClientEmail = useSelector((state) => state.ApiData.ClientEmail);
  const [securePass , setSecurePass] = useState(true);
  const [secureConfirmPass , setSecureConfirmPass] = useState(true);
  const change_Password = () => {
    //console.log(ClientEmail, password);

    if (password != "" && confirmPass != "") {
      if (password == confirmPass) {
        if (password.length < 8) {
          alert("Password limit should be greater than 8 digits");
        setIsLoading(false);

        } 
        else{
          fetch(URL + "/change_password_phone/", {
            method: "POST",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
  
            body: JSON.stringify({
              username: ClientEmail,
              password: password,
            }),
          })
            .then(async (response) => {
              let data = await response.json();
              //console.log("signup", data);
  
              //console.log("signup", response);
              if (response.status == 200) {
                alert(data.message);
                // Toast.show(data.message, Toast.LONG);
                setPassword("");
                setConfirmPass("");
                navigation.navigate("Login");
              } else {
                alert(data.message);
                // Toast.show(data.message, Toast.LONG);
                setPassword("");
                setConfirmPass("");
  
                //  alert(data.message);
              }
              //send_Verification_Code()
              // navigation.navigate("Ver
  
              //setResponse(json);
            })
            .catch((error) => console.log(error));
        }
        
      } else {
        alert("Password and confirm password not match")
        // Toast.show("Password And Confirm Password Not Match", Toast.LONG);
      }
    } else {
      alert("All fields are required")
      // Toast.show("All Fields Are Required", Toast.LONG);
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
            CHANGE
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

     
      <View style={{ ...styles.inputArea, marginTop: 40 }}>
        <TextInput
          style={{width:"95%"}}
          placeholder="Enter New Password"
          autoCapitalize="none"
          required={true}
          secureTextEntry={securePass}
          placeholderTextColor={Colors.productGrey}
          minLength={6}
          errorMessage="Please enter Minimum 6 characters password"
          value={password}
          onChangeText={(value) => setPassword(value)}
          initialValue=""
        />
        <View style={{alignSelf:"center",}}>
            <Icon active name={securePass?'eye':"eye-off"} color= {Colors.textGreyColor} size={25} 
                 onPress = {() => {
               
                  if(securePass == true){
                 setSecurePass(false)
                  }
                  else{
                    setSecurePass(true)
                  }
                }
                }
                 />
              </View>
      </View>
      <View style={styles.inputArea}>
        <TextInput
          style={{width:"95%"}}
          placeholder="Confirm Password"
          autoCapitalize="none"
          required={true}
          secureTextEntry={secureConfirmPass}
          placeholderTextColor={Colors.productGrey}
          minLength={6}
          errorMessage="Please enter Minimum 6 characters password"
          value={confirmPass}
          onChangeText={(value) => setConfirmPass(value)}
          initialValue=""
        />
        <View style={{alignSelf:"center",}}>
            <Icon active name={secureConfirmPass?'eye':"eye-off"} color= {Colors.textGreyColor} size={25} 
                 onPress = {() => {
               
                  if(secureConfirmPass == true){
                    setSecureConfirmPass(false)
                  }
                  else{
                    setSecureConfirmPass(true)
                  }
                }
                }
                 />
              </View>
      </View>

      <TouchableOpacity onPress={change_Password} style={styles.button}>
        <Text
          style={{
            color: "white",
            fontWeight: "bold",
            textAlign: "center",
            fontSize: 16,
          }}
        >
          SUBMIT
        </Text>
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
  },
});

export default ChangeForgotPassword;
