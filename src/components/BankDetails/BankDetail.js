// // import React, { Component } from "react";
// // import { useState, useEffect } from "react";
// // import {
// //   Image,
// //   ScrollView,
// //   ActivityIndicator,
// //   FlatList,
// //   TouchableHighlight,
// //   TouchableOpacity,
// //   ImageBackground,
// //   StyleSheet,
// //   KeyboardAvoidingView,
// //   TextInput,
// // } from "react-native";
// // import {
// //   Container,
// //   Header,
// //   Spinner,
// //   Card,
// //   CardItem,
// //   Thumbnail,
// //   Text,
// //   Title,
// //   Button,
// //   Left,
// //   Body,
// //   Right,
// //   View,
// // } from "native-base";
// // import Colors from "../../ColorCodes/Colors";
// // //import ViewShot from "react-native-view-shot";
// // import Ionicons from "react-native-vector-icons/Ionicons";
// // import FontAwesome from "react-native-vector-icons/FontAwesome";
// // import URL from "../../api/ApiURL";
// // import MyHeader from "../../components/MyHeader";

// // const BankDetail = ({ navigation, route }) => {
// //   return (
// //     <View style={{ flex: 1, height: "100%" }}>
// //       <View style={{ height: "30%" }}>
// //         <ImageBackground
// //           source={require("../../assets/Splash.jpg")}
// //           style={{
// //             width: "100%",
// //             height: "100%",
// //             justifyContent: "center",
// //             alignItems: "center",
// //           }}
// //         >
// //           <Text
// //             style={{
// //               color: "white",
// //               fontSize: 25,
// //               fontWeight: "bold",
// //               letterSpacing: 2,
// //             }}
// //           >
// //             BANK DETAILS
// //           </Text>
// //           <View
// //             style={{
// //               borderBottomColor: "white",
// //               borderBottomWidth: 0.5,
// //               width: "20%",
// //               marginTop: 10,
// //             }}
// //           ></View>
// //           <Text
// //             style={{
// //               color: Colors.yellowColor,
// //               marginTop: 20,
// //               fontSize: 12,
// //               fontWeight: "bold",
// //               letterSpacing: 2,
// //             }}
// //           >
// //             Enter Your Bank Details
// //           </Text>
// //         </ImageBackground>
// //       </View>

// //       <View style={{ height: "40%", paddingTop: 20 }}>
// //         <KeyboardAvoidingView behavior="padding" keyboardVerticalOffset={50}>
// //           {/*  */}

// //           {/* <FormSignup type="SignUp"/> */}

// //           <View style={styles.inputArea}>
// //             <TextInput
// //               style={{ width: 250 }}
// //               placeholder="Bank Name"
// //               autoCapitalize="none"
// //               required={true}
// //               placeholderTextColor={Colors.productGrey}
// //               minLength={6}
// //               errorMessage="Please enter Minimum 6 characters password"
// //               initialValue=""
// //             />
// //           </View>
// //           <View style={styles.inputArea}>
// //             <TextInput
// //               style={{ width: 250 }}
// //               placeholder="Branch Code"
// //               autoCapitalize="none"
// //               required={true}
// //               placeholderTextColor={Colors.productGrey}
// //               minLength={6}
// //               errorMessage="Please enter Minimum 6 characters password"
// //               initialValue=""
// //             />
// //           </View>
// //           <View style={styles.inputArea}>
// //             <TextInput
// //               style={{ width: 250 }}
// //               placeholder="Card Number"
// //               autoCapitalize="none"
// //               required={true}
// //               placeholderTextColor={Colors.productGrey}
// //               minLength={6}
// //               errorMessage="Please enter Minimum 6 characters password"
// //               initialValue=""
// //             />
// //           </View>
// //           <View style={styles.inputArea}>
// //             <TextInput
// //               style={{ width: 250 }}
// //               placeholder="Sort Code"
// //               autoCapitalize="none"
// //               required={true}
// //               placeholderTextColor={Colors.productGrey}
// //               minLength={6}
// //               errorMessage="Please enter Minimum 6 characters password"
// //               initialValue=""
// //             />
// //           </View>
// //           <View style={styles.inputArea}>
// //             <TextInput
// //               style={{ width: 250 }}
// //               placeholder="Card Expiry Date"
// //               autoCapitalize="none"
// //               required={true}
// //               placeholderTextColor={Colors.productGrey}
// //               minLength={6}
// //               errorMessage="Please enter Minimum 6 characters password"
// //               initialValue=""
// //             />
// //           </View>

// //           <TouchableOpacity style={styles.button}>
// //             <Text
// //               style={{
// //                 color: "white",
// //                 fontWeight: "bold",
// //                 textAlign: "center",
// //                 fontSize: 16,
// //               }}
// //             >
// //               SUBMIT
// //             </Text>
// //           </TouchableOpacity>
// //         </KeyboardAvoidingView>
// //       </View>
// //     </View>
// //   );
// // };
// // const styles = StyleSheet.create({
// //   name_inputArea: {
// //     height: 40,
// //     width: 130,

// //     backgroundColor: "#E2E2E2",
// //     borderRadius: 25,
// //     paddingHorizontal: 30,
// //   },
// //   name2_inputArea: {
// //     marginLeft: 20,
// //     marginVertical: 10,
// //     height: 40,
// //     width: 135,
// //     backgroundColor: "#E2E2E2",
// //     borderRadius: 25,
// //     paddingHorizontal: 30,
// //   },
// //   inputArea: {
// //     marginVertical: 5,
// //     alignSelf: "center",
// //     height: 40,
// //     width: 280,
// //     backgroundColor: "#E2E2E2",
// //     borderRadius: 25,
// //     paddingHorizontal: 30,
// //     flexDirection: "row",
// //   },

// //   button: {
// //     height: 40,
// //     width: 270,
// //     backgroundColor: "#EE0202",
// //     justifyContent: "center",
// //     borderRadius: 25,
// //     marginVertical: 20,
// //     alignSelf: "center",
// //   },
// // });
// // export default BankDetail;
// import React,{useEffect,useState} from 'react';
// import {View,Text,Image,ImageBackground,TouchableOpacity, StyleSheet,ScrollView,FlatList,LogBox} from 'react-native';
// import Card from '../Card';
// import {
// Container,
// Header,
// Spinner,
// } from "native-base";
// import FontAwesome from 'react-native-vector-icons/FontAwesome';
// import Colors from '../../ColorCodes/Colors';
// import URL from  '../../api/ApiURL'
// function BankDetail({navigation}) {
// const [packageData,setPackageData]=useState("");
// const [imagePackage,setImagePackage]=useState("");
// const [loading,setLoading]=useState(false);
// useEffect(() => {
// LogBox.ignoreLogs(['Failed child context type']);

// setLoading(true);
// fetch(URL+'/delivery_person/list_packages/')
// // fetch(URL+'/client_app/clients_list/33/')
// .then((response) => response.json())
// .then((responseJson) => {

// console.log("Packages:",responseJson);
// setPackageData(responseJson.all_package);
// setLoading(false);

// // console.log("Dashboard:",responseJson.client_dashboard.client_name);
// //console.log("Buisness Detail:",responseJson.client_businesses[0]['name']);
// // if (json["response"] == "Record does not exist or not found") {
// // setLoading(true);
// // } else {
// // dispatch(ApiDataAction.SetListData(responseJson));
// // dataa=responseJson;
// // setData(responseJson);
// // //console.log(json);

// // }
// })
// .catch((error) => console.error(error))
// }, [])





// return (
// <View style={{flex:1,height:"100%",justifyContent:'space-around'}}>
// {/* {/ <ScrollView> /} */}
// {loading ? (
// <Spinner color={Colors.themeColor} size={50} />

// ) :
// <FlatList
// data={packageData}
// keyExtractor={item => item.id}
// style={{width:'100%'}}
// renderItem={itemData => (
// <TouchableOpacity onPress={()=>navigation.navigate("PaymentMethods")} style={{width:'90%',alignSelf:'center',marginTop:10,bottom:5}}>
// <ImageBackground

// source={itemData.item.name=="Basic" ?require(`.../../assets/Basic.png`):itemData.item.name=="Silver" ?require(`../../assets/Silver.png`):itemData.item.name=="Gold" ?require(`../../assets/Gold.png`):itemData.item.name=="Platinum" ?require(`../../assets/Platinum.png`):null}
// style={{ width: "100%", height:130}}
// >
// <View style={{height:"100%"}}>
// <View style={{height:"48%",width:'75%',justifyContent:'center'}}>

// <Text style={{color:'white',fontSize:18,textAlign:'center',fontWeight:'100',letterSpacing:1}}>{itemData.item.name.toUpperCase()}</Text>


// </View>
// <View style={{height:"53%",width:"100%",flexDirection:'row'}}>
// <View style={{width:"50%",justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{itemData.item.no_of_invoices}</Text>

// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>INVOICES</Text>

// </View>
// <View style={{width:"50%",justifyContent:'center'}}>
// <View style={{flexDirection:'row',justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{itemData.item.price}</Text>
// <Text style={{color:'white',fontSize:14,paddingTop:10,paddingLeft:2}}>£</Text>
// </View>
// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>PRICE</Text>

// </View>
// </View>

// </View>


// </ImageBackground>

// </TouchableOpacity>
// )}
// />
// }








// {/* <TouchableOpacity style={{height:'22%',width:'90%',alignSelf:'center'}}>
// <ImageBackground
// source={require("../assets/silver.png")}
// style={{ width: "100%", height: "100%" }}
// >
// <View style={{height:"100%"}}>
// <View style={{height:"48%",width:'75%',justifyContent:'center'}}>

// <Text style={{color:'white',fontSize:18,textAlign:'center',fontWeight:'100',letterSpacing:1}}>{packageData["all_package"][0]["name"].toUpperCase()}</Text>


// </View>
// <View style={{height:"53%",width:"100%",flexDirection:'row'}}>
// <View style={{width:"50%",justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{packageData["all_package"][0]["no_of_invoices"]}</Text>

// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>INVOICES</Text>

// </View>
// <View style={{width:"50%",justifyContent:'center'}}>
// <View style={{flexDirection:'row',justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{packageData["all_package"][0]["price"]}</Text>
// <Text style={{color:'white',fontSize:14,paddingTop:10,paddingLeft:2}}>£</Text>
// </View>
// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>PRICE</Text>

// </View>
// </View>

// </View>


// </ImageBackground>

// </TouchableOpacity>


// <TouchableOpacity style={{height:'22%',width:'90%',alignSelf:'center'}}>
// <ImageBackground
// source={require("../assets/gold.png")}
// style={{ width: "100%", height: "100%" }}
// >
// <View style={{height:"100%"}}>
// <View style={{height:"48%",width:'75%',justifyContent:'center'}}>

// <Text style={{color:'white',fontSize:18,textAlign:'center',fontWeight:'100',letterSpacing:1}}>{packageData["all_package"][2]["name"].toUpperCase()}</Text>


// </View>
// <View style={{height:"53%",width:"100%",flexDirection:'row'}}>
// <View style={{width:"50%",justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{packageData["all_package"][2]["no_of_invoices"]}</Text>

// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>INVOICES</Text>

// </View>
// <View style={{width:"50%",justifyContent:'center'}}>
// <View style={{flexDirection:'row',justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{packageData["all_package"][2]["price"]}</Text>
// <Text style={{color:'white',fontSize:14,paddingTop:10,paddingLeft:2}}>£</Text>
// </View>
// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>PRICE</Text>

// </View>
// </View>

// </View>


// </ImageBackground>

// </TouchableOpacity>


// <TouchableOpacity style={{height:'22%',width:'90%',alignSelf:'center'}}>
// <ImageBackground
// source={require("../assets/platinum.png")}
// style={{ width: "100%", height: "100%" }}
// >
// <View style={{height:"100%"}}>
// <View style={{height:"48%",width:'75%',justifyContent:'center'}}>

// <Text style={{color:'white',fontSize:18,textAlign:'center',fontWeight:'100',letterSpacing:1}}>{packageData["all_package"][3]["name"].toUpperCase()}</Text>


// </View>
// <View style={{height:"53%",width:"100%",flexDirection:'row'}}>
// <View style={{width:"50%",justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{packageData["all_package"][3]["no_of_invoices"]}</Text>

// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>INVOICES</Text>

// </View>
// <View style={{width:"50%",justifyContent:'center'}}>
// <View style={{flexDirection:'row',justifyContent:'center'}}>
// <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{packageData["all_package"][3]["price"]}</Text>
// <Text style={{color:'white',fontSize:14,paddingTop:10,paddingLeft:2}}>£</Text>
// </View>
// <Text style={{color:'white',fontSize:10,textAlign:'center'}}>PRICE</Text>

// </View>
// </View>

// </View>


// </ImageBackground>

// </TouchableOpacity> */}
// </View>
// )
// }


// const styles = StyleSheet.create({
// cartItem: {
// flex: 1,
// marginTop:12,
// padding: 10,
// backgroundColor: 'white',
// borderWidth: .5,
// borderColor: "#EE0202",
// flexDirection: 'row',
// justifyContent: 'space-between',
// marginHorizontal: 20,
// borderRadius:15
// },
// })

// export default BankDetail
