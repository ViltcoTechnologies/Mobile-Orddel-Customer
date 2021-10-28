import React from "react";
import { useState } from "react";
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Image,
  StatusBar,
  TouchableOpacity,
} from "react-native";
import AsyncStorage from "@react-native-community/async-storage";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Ionicons from "react-native-vector-icons/Ionicons";
import Entypo from "react-native-vector-icons/Entypo";
import SimpleLineIcons from "react-native-vector-icons/SimpleLineIcons";
import AntDesign from "react-native-vector-icons/AntDesign";
import { useSelector, useDispatch } from "react-redux";
import * as ApiDataAction from "../../store/actions/ApiData";
import { DrawerContentScrollView, DrawerItem } from "@react-navigation/drawer";
import {
  Container,
  Header,
  Content,
  Thumbnail,
  Text,
  Label,
  Drawer,
} from "native-base";
import Colors from "../../ColorCodes/Colors";
import { Icon } from "react-native-elements";

const DrawerContent = (props) => {
  const dispatch=useDispatch();
  const ClientName = useSelector((state) => state.ApiData.ClientName);
  const ClientImage = useSelector((state) => state.ApiData.ClientImage);
  const ClientId = useSelector((state) => state.ApiData.ClientId);
  const [checkRemember,setCheckRemember]=useState(false);

  var getToken = async () => {
    console.log("Hi Shaheer Welcome to Hell");

    try {
      let check = await AsyncStorage.getItem("remember");
      let datal = JSON.parse(check);
      console.log("remember11111:",datal)
//               if(checkRemember){
//                 AsyncStorage.removeItem("loginCheck");
//               }
//               else{
//                 AsyncStorage.clear();
// //  AsyncStorage.removeItem("userData");
// //               AsyncStorage.removeItem("passData");
// //               AsyncStorage.removeItem("loginCheck");
//               }
     
      if(datal){
      // setLoading(true)
      AsyncStorage.removeItem("loginCheck");
      }
      else{
        console.log("from Else jajajajaj")
//  AsyncStorage.removeItem("userData");
//               AsyncStorage.removeItem("passData");
//               AsyncStorage.removeItem("loginCheck");
              AsyncStorage.clear();
      }
      
      
     
    } catch (error) {
      console.log("Something went wrong", error);
    }
  };
  // const route = props
  //   const [companyInfo,     setCompanyInfo] = useState([route.initialParams['params']['Company_Data'][0][0]])
  //   const [personInfo,       setPersonInfo] = useState([route.initialParams['params']['Company_Data'][1]]);
  //   const [contactPerson, setContactPerson] = useState([route.initialParams['params']['Company_Data'][2]]);
  //   const [accountInfo,     setaccountInfo] = useState([route.initialParams['params']['Company_Data'][3]]);
  //   const [login , setLogin] = useState([[companyInfo][0][0]["login"]])
  //   const [password , setPassword] = useState([[companyInfo][0][0]["password"]])
  //   const [shipperID , setShipperID] = useState([[companyInfo][0][0]["id"]])
  //   const image_Base64=companyInfo[0]["get_image_base64"];
  //console.log(companyInfo[0]["get_image_base64"])

  return (
    <View style={{ flex: 1 }}>
      <DrawerContentScrollView style={{ backgroundColor: "white" }} {...props}>
        <Content>
          <TouchableOpacity
            onPress={() => props.navigation.navigate("Profile")}
          >
            <View style={{ alignItems: "center" }}>
              <Thumbnail
                scaleX={1.3}
                scaleY={1.3}
                style={{ margin: 20 }}
                source={
                  ClientImage == ""||ClientImage==null
                    ? require("../../assets/profilelogo.png")
                    : { uri: ClientImage }
                }
              />

              <Text
                style={{ fontWeight: "bold", color: "black", fontSize: 18 }}
              >
                {ClientName}
              </Text>
            </View>
            {/* <View style = {{alignItems:'center'}}>
          <Text style ={{fontWeight:'bold',color:'black',padding:5}}>Khan</Text>
          </View> */}
          </TouchableOpacity>
        </Content>

        <View
          style={{
            marginTop: 35,
            marginLeft: 15,
            borderBottomColor: Colors.bottomLine,
            borderBottomWidth: 1,
            width: 240,
          }}
        >
          <TouchableOpacity
            onPress={() => props.navigation.navigate("Dashboard")}
            style={{ flexDirection: "row", marginBottom: 10 }}
          >
            <MaterialCommunityIcons
              name="home"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 10 }}
            />
            <Text
              style={{ marginLeft: 20, fontSize: 16, color: Colors.textBlack }}
            >
              Home
            </Text>
            <MaterialIcons
              name="navigate-next"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 130 }}
            />
          </TouchableOpacity>
        </View>

        <View
          style={{
            marginTop: 20,
            marginLeft: 15,
            borderBottomColor: Colors.bottomLine,
            borderBottomWidth: 1,
            width: 240,
          }}
        >
          <TouchableOpacity
            onPress={() => props.navigation.navigate("BuisnessDetail")}
            style={{ flexDirection: "row", marginBottom: 10 }}
          >
            <AntDesign
              name="form"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 10 }}
            />
            <Text
              style={{ marginLeft: 20, fontSize: 16, color: Colors.textBlack }}
            >
              Business Details
            </Text>
            <MaterialIcons
              name="navigate-next"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 60 }}
            />
          </TouchableOpacity>
        </View>

        {/* <View style={{ marginTop:20,marginLeft:15,borderBottomColor:Colors.bottomLine,borderBottomWidth:1,width:240}}>
        
        <TouchableOpacity onPress={()=>props.navigation.navigate("Packages")} style={{flexDirection:'row',marginBottom:10}}>
            <Image source={require("../../assets/d_package.png")} style={{width:25,height:25,marginLeft:3}} />
        
        <Text style={{marginLeft:20,fontSize:16,color:Colors.textBlack}}>Packages</Text>
        <MaterialIcons name="navigate-next" color = {Colors.textBlack} size={Platform.OS=='android'?20:20} style={{marginLeft:105}} />
        </TouchableOpacity>
        
        </View> */} 

        {/* <View style={{ marginTop:20,marginLeft:15,borderBottomColor:Colors.bottomLine,borderBottomWidth:1,width:240}}>
        
        <TouchableOpacity onPress={()=>props.navigation.navigate("ShippmentAddresses")} style={{flexDirection:'row',marginBottom:10}}>
        <Entypo name="location" color = {Colors.textBlack} size={Platform.OS=='android'?20:70} style={{marginLeft:10}}/>
        <Text style={{marginLeft:20,fontSize:16,color:Colors.textBlack}}>Shippment Addresses</Text>
        <MaterialIcons name="navigate-next" color = {Colors.textBlack} size={Platform.OS=='android'?20:70} style={{marginLeft:15}} />
        </TouchableOpacity>
        
        </View> */}

        <View
          style={{
            marginTop: 20,
            marginLeft: 15,
            borderBottomColor: Colors.bottomLine,
            borderBottomWidth: 1,
            width: 240,
          }}
        >
          <TouchableOpacity
            onPress={() => props.navigation.navigate("Support")}
            style={{ flexDirection: "row", marginBottom: 10 }}
          >
            <SimpleLineIcons
              name="docs"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 10 }}
            />
            <Text
              style={{ marginLeft: 20, fontSize: 16, color: Colors.textBlack }}
            >
              Support
            </Text>
            <MaterialIcons
              name="navigate-next"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 115 }}
            />
          </TouchableOpacity>
        </View>

        <View style={{ marginTop: 20, marginLeft: 15, width: 240 }}>
          <TouchableOpacity
            onPress={() => {
              dispatch(ApiDataAction.Clear_All(1));
              getToken();
              // let check = AsyncStorage.getItem("remember");
              // let datal = JSON.parse(check);
             
             

            // AsyncStorage.clear();
               props.navigation.navigate("Login");
            }}
            style={{ flexDirection: "row", marginBottom: 10 }}
          >
            <MaterialCommunityIcons
              name="logout"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 10 }}
            />
            <Text
              style={{ marginLeft: 20, fontSize: 16, color: Colors.textBlack }}
            >
              Log Out
            </Text>
            <MaterialIcons
              name="navigate-next"
              color={Colors.textBlack}
              size={Platform.OS == "android" ? 20 : 20}
              style={{ marginLeft: 115 }}
            />
          </TouchableOpacity>
        </View>

       
      </DrawerContentScrollView>
     
    </View>
  );
};
const styles = StyleSheet.create({
  logo: {
    height: 100,
    width: "100%",
    justifyContent: "center",
    alignItems: "center",
  },
});

export default DrawerContent;
