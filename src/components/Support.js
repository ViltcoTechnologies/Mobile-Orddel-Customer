import React, { useEffect } from "react";
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
  BackHandler,
  Linking
} from "react-native";
import Ionicons from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Colors from "../ColorCodes/Colors";
import MyHeader from "../components/MyHeader";
import { useRoute, useFocusEffect } from "@react-navigation/native";

const Support = ({ navigation,route }) => {
  useFocusEffect(
    React.useCallback(() => {
      const backAction = () => {
        navigation.navigate("Dashboard")
        // Alert.alert("Hold on!", "Are you sure you want to go back?", [
        //   {
        //     text: "Cancel",
        //     onPress: () => null,
        //     style: "cancel"
        //   },
        //   { text: "YES", onPress: () => BackHandler.exitApp() }
        // ]);
        return true;
      };
  
      const backHandler = BackHandler.addEventListener(
        "hardwareBackPress",
        backAction
      );
  
      return () => backHandler.remove();
    }, [route])
  );
  return (
    <View style={{ flex: 1, height: "100%", backgroundColor: "white" }}>
      {/* <MyHeader name="SUPPORT" nav={navigation} /> */}

      <View
        style={{
          height: "55%",
          top: Platform.OS == "ios" ? 50 : 20,

          //justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Image
          source={require("../assets/supportscreen.png")}
          style={{
            width: 240,
            height: 220,
          }}
        />
      </View>
      <View
        style={{
          height: "35%",
          bottom: 10,

          width: "90%",
          alignSelf: "center",
          //justifyContent: "center",
          //alignItems: "center",
          //flexDirection: "row",
        }}
      >
        <View
          style={{
            borderBottomColor: "lightgray",
            borderBottomWidth: 1,
          }}
        ></View>
        <View
          style={{
            width: "100%",
            height: "30%",

            flexDirection: "row",
          }}
        >
          <View
            style={{
              width: "30%",
              height: "100%",

              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <Image
              source={require("../assets/phone.png")}
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

              justifyContent: "center",
            }}
          >
            <TouchableOpacity onPress={()=>Linking.openURL(`tel:$+(44)2033556560`)}>

            <Text style={{ color: Colors.textGreyColor }}>Phone Number</Text>
            <Text
              style={{
                color: Colors.themeColor,
                fontSize: 18,
                fontWeight: "bold",
              }}
            >
              +(44)2033556560
            </Text>
            </TouchableOpacity>
          </View>
        </View>
        <View
          style={{
            borderBottomColor: "lightgray",
            borderBottomWidth: 1,
          }}
        ></View>
        <View
          style={{
            width: "100%",
            height: "30%",

            flexDirection: "row",
          }}
        >
          <View
            style={{
              width: "30%",
              height: "100%",

              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <Image
              source={require("../assets/eemail.png")}
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

              justifyContent: "center",
            }}
          >
            <Text style={{ color: Colors.textGreyColor }}>Email Address</Text>
            <Text
              style={{
                color: Colors.themeColor,
                fontSize: 18,
                fontWeight: "bold",
              }}
            >
              support@orddel.co.uk
            </Text>
          </View>
        </View>
        <View
          style={{
            borderBottomColor: "lightgray",
            borderBottomWidth: 1,
          }}
        ></View>

        <View
          style={{
            width: "100%",
            height: "30%",

            flexDirection: "row",
          }}
        >
          <View
            style={{
              width: "30%",
              height: "100%",

              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <Image
              source={require("../assets/website.png")}
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

              justifyContent: "center",
            }}
          >
            <TouchableOpacity onPress={()=>Linking.openURL("https://orddel.co.uk/")}>

            <Text style={{ color: Colors.textGreyColor }}>Website</Text>
            <Text
              style={{
                color: Colors.themeColor,
                fontSize: 18,
                fontWeight: "bold",
              }}
            >
              www.orddel.co.uk
            </Text>
            </TouchableOpacity>
          </View>
        </View>
      </View>
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
});

export default Support;
