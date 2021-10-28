import React, { useState,useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  Platform,
  TextInput,
  BackHandler
} from "react-native";
import {
  TouchableNativeFeedback,
  TouchableHighlight,
  TouchableOpacity,
  TouchableWithoutFeedback,
} from 'react-native-gesture-handler';
import Ionicons from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Colors from "../ColorCodes/Colors";
import { useSelector, useDispatch } from 'react-redux';
import * as cartActions from "../store/actions/OrderBox";
import { useRoute, useFocusEffect } from "@react-navigation/native";
const CartItem = (props,{route}) => {


  const dispatch=useDispatch();
  const [qtty,setQtty]=useState("");
  const MyIcon1 = <FontAwesome name="minus" size={15} color="#EE0202" solid />;
  const MyIcon2 = <FontAwesome name="plus" size={15} color="#EE0202" solid />;
  let reg = /^\d+$/;
  
  const updateTotalAmount=()=>{
    
    alert("Key edit")

    if(qtty!=""){
     
        if (qtty == "") {
            // dropDownAlertRef.alertWithType('error', '', "Please Enter Quantity.");

            // alert("Please Enter Quantity.");
          }
          else if(reg.test(qtty) === false) {

            // alert("Invalid Quantity");
            setQtty("");
              return false;
          }
          else if(qtty==0) {

            // alert("Invalid Quantity");
            setQtty("");
          }
          else {
            dispatch(
              cartActions.updateTotal(props.id, qtty)
            )
       
            }
        
    }
    }




  const updateQuantity=(qtty)=>{
    // alert("Key Press")
    console.log(qtty)

    if(qtty!=""){
     
        if (qtty == "") {
            // dropDownAlertRef.alertWithType('error', '', "Please Enter Quantity.");

            alert("Please enter quantity.");
          }
          else if(reg.test(qtty) === false) {

            alert("Invalid quantity");
            setQtty("");
              return false;
          }
          else if(qtty==0) {

            alert("Invalid quantity");
            setQtty("");
          }
          else {
            dispatch(
              cartActions.updateQtty(props.id, qtty)
            )
            // dispatch(
            //   cartActions.updateTotal(props.id, qtty)
            // )
            
            }
        
    }
    }
  

  return (
    <View
      style={{
        flexDirection: "row",
        borderBottomWidth: 0.5,
        borderBottomColor: "grey",
        marginTop: 10,
        width: "100%",
        
      }}
    >
      
      <View style={{ width: "30%", justifyContent: "center" }}>
        <Text
          style={{
            marginLeft: 2,
            color: Colors.productGrey,
            textAlign: 'left',
          }}
        >
          {props.name}
        </Text>
      </View>
      <View style={{ width: "20%", justifyContent: "center" }}>
        <Text style={{ color: Colors.productGrey, textAlign: "center" }}>
          {props.unit}
        </Text>
      </View>
      <View style={{width:'20%',alignSelf:"center"}}>

<TextInput
style={{alignSelf:"center",color:Colors.productGrey,paddingBottom:0,textAlign:'right',}}
// hitSlop={{ top: 30, bottom: 30, left: 30, right: 30 }}
placeholder={props.quantity.toString()}
autoCapitalize="none"
keyboardType="numeric"
maxLength={2}
placeholderTextColor={Colors.productGrey}
value={qtty}

// required={true}
onChangeText={(value) => {
    
  setQtty(value);
  //updateQuantity();
  updateQuantity(value)
//   setCheck(true);
   
}}

selectTextOnFocus={true}

initialValue=""
/>
</View>

      <View style={{ width: "22%", justifyContent: "center", }}>
        {props.price==0?<Text style={{ color: Colors.textGreyColor, textAlign: "right",marginRight:8 }}>
          £ {props.price}
        </Text>:<Text style={{ color: Colors.textGreyColor, textAlign: "right",marginRight:8 }}>
          £ {parseFloat(props.price).toFixed(2)}
        </Text>}
      </View>

      {/* {props.addable && ( */}
      <TouchableOpacity
        onPress={props.onDelete}
        style={{ alignItems: "center", justifyContent: "center" }}
        // hitSlop={{ top: 30, bottom: 30, left: 30, right: 30 }}
        // style={styles.deleteButton}
      >
        <Ionicons
          name={Platform.OS === "android" ? "md-trash" : "ios-trash"}
          size={25}
          color="#EE0202"
        />
      </TouchableOpacity>
      {/* )}  */}
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
  itemData: {
    flexDirection: "row",
    alignItems: "center",
  },
  quantity: {
    color: "#EE0202",
    fontWeight: "bold",
    fontSize: 18,
    marginRight: 4,
  },

  title: {
    fontFamily: "open-sans-bold",
    fontSize: 16,
    color: "orange",
    fontWeight: "bold",
  },

  rupees: {
    color: "black",
    //fontFamily: 'open-sans-bold',
    fontSize: 16,
  },

  deleteButton: {
    marginLeft: 10,
  },

  button: {
    marginLeft: 15,
  },
});

export default CartItem;
