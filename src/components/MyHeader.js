import React from "react";
import { View, Button, Text, Image, TouchableOpacity,Platform } from "react-native";
import Colors from "../ColorCodes/Colors";
import Ionicons from "react-native-vector-icons/Ionicons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import * as cartActions from "../store/actions/OrderBox";
import { useSelector, useDispatch } from "react-redux";
function MyHeader(props) {
  const dispatch=useDispatch();
  console.log(props, "props");
  return (
    <View
      style={{
        height: "10%",
        backgroundColor: Colors.themeColor,
        flexDirection: "row",
        marginTop:Platform.OS=="android"?20:0,
        paddingTop: 18,
        width: "100%",
      }}
    >
      <View
        style={{
          height: "100%",
          width: "15%",
          justifyContent: "center",
          paddingLeft: "5%",
          marginTop:Platform.OS=="android"?null:"2%"
        }}
      >
        <TouchableOpacity onPress={() => {dispatch(cartActions.allClear(1));

           props.nav.navigate("Dashboard");}} transparent>
          <MaterialCommunityIcons name="arrow-left" size={25} color="white" />
        </TouchableOpacity>
      </View>
      <View
        style={{
          height: "100%",
          width: "65%",
          justifyContent: "center",
          paddingLeft: Platform.OS=="android"?10:null,
          marginTop:Platform.OS=="android"?null:"2%",
          marginLeft:Platform.OS=="android"?null:"10%"
          
        }}
      >
        <Text
          style={{
            color: "white",
            fontWeight: "bold",
            textAlign: "center",
            width: 200,
            fontSize: 18,
          }}
        >
          {props.name}
        </Text>
      </View>
      <View style={{ height: "100%", width: "20%", justifyContent: "center",paddingLeft:Platform.OS=="android"?20:0 }}>
        <Image
          source={require("../assets/colorLogo.png")}
          style={{
            width: Platform.OS == "ios" ? 40 : 50,
            height: Platform.OS == "ios" ? 40 : 50,
            marginBottom:Platform.OS=="android"?5:0,
            marginTop:Platform.OS=="android"?0:10
            
          }}
        />
      </View>
    </View>
  );
}

export default MyHeader;
