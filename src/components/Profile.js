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
  Modal,
  BackHandler
} from "react-native";
import Card from '../components/Card'
import Icon from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Colors from "../ColorCodes/Colors";
import MyHeader from "../components/MyHeader";
import URL from "../../src/api/ApiURL";
import { useSelector, useDispatch } from "react-redux";
import { useIsFocused } from "@react-navigation/native";
import { useRoute, useFocusEffect } from "@react-navigation/native";

import * as ApiDataAction from "../store/actions/ApiData";
import base64 from "react-native-base64";
// import Toast from "react-native-simple-toast";


import DocumentPicker from "react-native-document-picker";

import MaterialIcons from "react-native-vector-icons/MaterialIcons";
import {launchCamera, launchImageLibrary} from 'react-native-image-picker';
import ImagePicker from 'react-native-image-crop-picker';


const Profile = ({ navigation,route }) => {
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
  const dispatch = useDispatch();
  const [modalVisible, setModalVisible] = useState(false);
  const [imageLoading, setImageLoading] = useState(false);

  const [photoState, setPhotoState] = useState("");

  const ClientId = useSelector((state) => state.ApiData.ClientId);
  const ClientPackage = useSelector((state) => state.ApiData.ClientPackage);
  const ClientEmail = useSelector((state) => state.ApiData.ClientEmail);
  const FirstName = useSelector((state) => state.ApiData.FirstName);
  const LastName = useSelector((state) => state.ApiData.LastName);
  const UsedInvoices = useSelector((state) => state.ApiData.UsedInvoices);
  const PhoneNumber = useSelector((state) => state.ApiData.ClientPhone);
  const ClientImage = useSelector((state) => state.ApiData.ClientImage);
  const RemainingInvoices = useSelector(
    (state) => state.ApiData.RemainingInvoices
  );

  const isFocused = useIsFocused();

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [phoneNo, setPhoneNo] = useState("");
  const [oldSecurePass , setOldSecurePass] = useState(true);
  const [securePass , setSecurePass] = useState(true);
  const [secureConfirmPass , setSecureConfirmPass] = useState(true);
  const [oldPass, setOldPass] = useState("");
  const [newPass, setNewPass] = useState("");
  const [confirmPass, setConfirmPass] = useState("");

  const [response, setResponse] = useState("");
  const [data, setData] = useState("");

  var dataa = 0;

  const handlePhoto = async () => {

    
    const options = {
      noData: true,
    };
     var res = 0;
     
    //  const result =await request(PERMISSIONS.IOS.PHOTO_LIBRARY);
    //  if ("granted" === result) {
    //   alert(result)
      //console.log(result,'....permission ios......');
      let pathToFile = "file:///var/mobile/Containers/Data/Application/9793A9C3-C666-4A0E-B630-C94F02E32BE4/Documents/images/72706B9A-12DF-4196-A3BE-6F17C61CAD06.jpg"
      
    try {
      res = await DocumentPicker.pick({
        type: [DocumentPicker.types.images],
        //type: [DocumentPicker.types.allFiles]
      });

    //   if (Platform.OS === 'ios') {
    //     //pathToFile = '~' + pathToFile.substring(pathToFile.indexOf('/Documents'));
    //     res.uri = '~' + res.uri.substring(res.uri.indexOf('/Documents'));
        
    // }
    
      setPhotoState({ photo: res });
      dispatch(ApiDataAction.SetImage(res.uri));

      uploadImage(res);

      // {"fileCopyUri": "content://com.android.providers.media.documents/document/image%3A27039", 
      // "name": "Screenshot_20210530_170709.jpg", "size": 668283, "type": "image/jpeg", 
      // "uri": "content://com.android.providers.media.documents/document/image%3A27039"} Imageee.......


      console.log(res, "Imageee.......");
      alert('Image updated successfully')
    } catch (err) {
      if (DocumentPicker.isCancel(err)) {
        // User cancelled the picker, exit any dialogs or menus and move on
      } else {
        throw err;
      }
    }
  // }
  // else{
  //   return;
  // }
    // const base64File = await RNFS.readFile(res.uri, "base64");
  };


// const handleChoosePhoto = () =>{

//   //alert('choose photo from libaray')
//   ImagePicker.openPicker({
//     width: 300,
//     height: 400,
//     //cropping: true
//   })
//   .then(image => {

//     setPhotoState({ photo: image });
//       //dispatch(ApiDataAction.SetImage(image.sourceURL));
//       dispatch(ApiDataAction.SetImage(image.path));
//       uploadImage(image);
//     console.log(image.path,'.........uri......... ');
//     alert('Image Updated successfully');
//   })
  

// }

  //-------------------New Handle Photo--------------------------//
const handleChoosePhoto = () => {
  const Options = {
    title: "Choose an Image",
    // includeBase64: true,
  };
  // launchCamera(Options, (response) => {
  //   setPhotoState({ photo: response });
  //   imageBase64 = response.base64;
  //   //console.log("base64", response.base64, "____________sh");
  //   console.log(response.uri, "----------------res");
  //   setCheckImage(true);
  //   setImageUri(response.uri);
  //   handleBase64(imageBase64);
  //   dispatch(ApiDataAction.SetImageUri(response.uri));
  // });
  launchImageLibrary(Options, (response) => {
    // setPhotoState({ photo: response });
    // imageBase64 = response.base64;
    if (response.didCancel) {
      // alert('User cancelled image picker');
    }
    else{

    setPhotoState({ photo: response });
    dispatch(ApiDataAction.SetImage(response.uri));

    uploadImage(response);
    console.log(response, "Imageee");
    }
    //  alert("Image updated successfully");

    // if(Platform.OS==='ios' )
    // {
    //   setPhotoState({ photo: response });
    // dispatch(ApiDataAction.SetImage(response.fileName));
    // }
    //console.log("base64", response.base64, "____________sh");
    //console.log(response.uri, "----------------res");
    // setCheckImage(true);
    // setImageUri(response.uri);
    // handleBase64(imageBase64);
    // dispatch(ApiDataAction.SetImageUri(response.uri));
  });
};

  const uploadImage = (response) => {
    var formdata = new FormData();
    formdata.append("image", response);
    formdata.append("id", ClientId);
    console.log(response.uri,'......uri.......');
//------------new add----------------//
    formdata.append("name", "image");
    formdata.append("image", {
      uri: response.uri,
      type: response.type,
      name: response.fileName,
    });


    var requestOptions = {
      method: "POST",
      body: formdata,
      redirect: "follow",
      headers: {
        "Content-Type": "multipart/form-data;",
      },
    };

    // alert("Image updated successfully");
    fetch(URL + "/client_app/upload_client_logo/", requestOptions)
      .then((response) => response.json())
      .then((result) =>
      {
      console.log(result,"----------true")
      //const { id } = result
      
      if(result.message == "Image uploaded successfully"){
        // console.log(result.message, "wefnewnifeif")
    alert(result.message);

      }
      else{
    //alert("Image size is very big!");
    alert("Image not selected!");
      }
      })
      .catch((error) => console.log("error", error));
  };

  useEffect(() => {
    setFirstName(FirstName);
    setLastName(LastName);
    //setPhoneNo(PhoneNumber);
    fetch(URL + "/client_app/client_dashboard/" + ClientId + "/")
      // fetch(URL+'/client_app/clients_list/33/')
      .then((response) => response.json())
      .then((responseJson) => {
        console.log(
          "Dashboard:",
          responseJson.client_dashboard.no_of_pending_orders
        );
        console.log("Dashboard:", responseJson);
        // console.log("Dashboard:",responseJson.client_dashboard.client_name);
        //console.log("Buisness Detail:",responseJson.client_businesses[0]['name']);
        // if (json["response"] == "Record does not exist or not found") {
        //   setLoading(true);
        // } else {
        // console.log("=======",)
        dispatch(ApiDataAction.SetListData(responseJson));
        dataa = responseJson;
        setData(responseJson);
        //   //console.log(json);
        // }
      })
      .catch((error) => console.error(error));

    if (ClientImage == "") {
      fetch(URL + "/client_app/get_client_logo/" + ClientId + "/")
        // fetch(URL+'/client_app/clients_list/33/')
        .then((response) => response.json())
        .then((responseJson) => {
          console.log(" Getting Image:...........", responseJson);
          dispatch(ApiDataAction.SetImage(responseJson.image));
          // setImageCheck(false);
          // setImage(responseJson.image);
        })
        .catch((error) => console.error(error));
    }
  }, [isFocused]);

  //---------------------------Change Password------------------------//
  const change_Password = () => {
    //console.log("ph o",Phone_No);
    //console.log(ClientEmail, oldPass, "--------------------Header");
    if (newPass != "" && oldPass != "" && confirmPass != "") {
      if (newPass == confirmPass) {
        if(newPass==oldPass){
          alert("There no change between old and new password");
          
        }
        else if (newPass.length < 8) {
          // setToastMessage("Password limit should be Greater than 6 Digits");
          alert("Password limit should be greater than 7 digits");
        }
        else{
          fetch(URL + "/api/change-password/", {
            method: "PUT",
            headers: {
              Accept: "application/json",
              Authorization:
                "Basic " + base64.encode(`${ClientEmail}:${oldPass}`),
              //   btoa({ username: ClientEmail, password: oldPass })
  
              "Content-Type": "application/json",
            },
  
            body: JSON.stringify({
              old_password: oldPass,
              new_password: newPass,
            }),
          })
            .then(async (response) => {
              let data = await response.json();
              //console.log("signup", data);
              //console.log("signup", response.message);
              if (response.status == 200) {
                //alert(data.message);
                setModalVisible(!modalVisible);
                alert(data.message)
                // Toast.show(data.message, Toast.LONG);
              } else {
                alert("Your old password is invalid");
                // Toast.show("Your Old Password Is Invalid", Toast.LONG);
              }
            })
            .catch((error) => console.log(error));
        } 
        
      } else {
        alert("Password and confirm password does not match")
        // Toast.show("Password and Confirm Password Doesnot Match", Toast.LONG);
      }
    } else {
      alert("All fields are required");
      // Toast.show("All Fields Are Required", Toast.LONG);
    }
  };

  const send_Verification_Code = () => {
    //console.log("ph o",Phone_No);

    fetch(URL + "/send_otp/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        phone_number: phoneNo,
      }),
    })
      .then((res) => res.json())
      .then((json) => {
        //console.log("Resend Response: ", json);

        if (json != "Verification code resent") {
          alert(
            "Please wait, there is request load on our server while sending verification code"
          );
        }

        setResponse(json);
      })
      .catch((error) => console.log(error));
  };

  const UpdateProfile = () => {
    
    console.log(FirstName, "-------------------new First Name");
    console.log(firstName, "-------------------Old Last Name");

    if(lastName==""&&firstName==""){
      alert("Nothing to change");
    }
    // else if(lastName==""&&firstName==FirstName){

    // }
    else{
      if (firstName != FirstName || lastName != LastName){
        // if(firstName!=""&&lastName!=""){
          fetch(URL + "/client_app/update_client/", {
            method: "PUT",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: ClientEmail,
              phone_number: PhoneNumber,
              first_name: firstName==""?FirstName:firstName,
              last_name: lastName==""?LastName:lastName,
            }),
          })
            .then(async (response) => {
              let data = await response.json();
              console.log(data);
    
              if (response.status == 200) {
                dispatch(ApiDataAction.UpdateProfile(firstName, lastName, phoneNo));
                setFirstName("");
                setLastName("");
                setPhoneNo("");
                navigation.navigate("Dashboard")
                alert("Successfully updated the record");
                // Toast.show("Successfully Updated the record", Toast.LONG);
                //console.log(PhoneNumber, phoneNo);
              } else {
                setFirstName("");
                setLastName("");
                setPhoneNo("");
                alert("Error updating profile");
                // Toast.show("Error Updating Profile", Toast.LONG);
    
                // console.log("status code",response.status)
                // console.log("status code",data)
                console.log(data, "---------------Profile");
              }
    
              // code that can access both here
            })
            .catch((error) => console.log("Something went wrong", error));
        // }
        // else{
        // Toast.show("You have not Updated anything", Toast.LONG);
  
        // }
        
      } else {
        alert("Nothing to update");
        // Toast.show("Nothing to Update", Toast.LONG);
      }
    }
    
  };

  return (
    <View style={{ flex: 1, height: "100%" }}>
      {/* <MyHeader name="PROFILE" nav={navigation} /> */}

      <View style={{ height: "28%" }}>
        <ImageBackground
          source={require("../assets/Splash.jpg")}
          style={{
            width: "100%",
            height: "90%",
            justifyContent: "flex-end",
            alignItems: "center",
          
          }}
        >
          
            <Image
              style={styles.avatar}
              source={
                ClientImage == null||ClientImage==""
                  ? require("../assets/profilelogo.png")
                  : { uri: ClientImage }
              }
            />
         
          <View
            style={{
            
              alignSelf: "center",
              // alignSelf:'flex-start',
              // justifyContent:"flex-start",
              marginBottom: Platform.OS == "ios" ? "20%" : 100,

              //marginBottom: "30%",
              marginLeft: "26%",
            }}
          >
            <TouchableOpacity
              // style={{marginRight:'10%'}}
              activeOpacity={0.5}
              onPress={handleChoosePhoto}
            >
              <FontAwesome
                name="camera"
                size={21}
                // style={styles.iconStyle}
                color="white"
                style={{ alignSelf: "center" }}
              />
            </TouchableOpacity>
          </View>
        </ImageBackground>
      </View>
      <View style={{ height: "65%" }}>
      <KeyboardAvoidingView style={{ flex: 1 }}
        behavior={Platform.OS == "ios" ? "padding" : null} >
      <ScrollView keyboardShouldPersistTaps="always" showsVerticalScrollIndicator={false}>


          <View style={{ height: "100%" }}>
            <View>
              {/*  */}

              {/* <FormSignup type="SignUp"/> */}
              <View
                style={{
                  flexDirection: "row",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                <TextInput
                  style={styles.name1_inputArea}
                  autoFocus={false}
                  placeholder={FirstName}
                  autoCapitalize="words"
                  // textContentType='emailAddress'
                  placeholderTextColor={Colors.productGrey}
                  value={firstName}
                  onChangeText={(value) => setFirstName(value)}
                  initialValue=""
                />

                <TextInput
                  style={styles.name2_inputArea}
                  placeholder={LastName}
                  autoFocus={false}
                  autoCapitalize="none"
                  autoCapitalize="words"
                  placeholderTextColor={Colors.productGrey}
                  value={lastName}
                  onChangeText={(value) => setLastName(value)}
                  initialValue=""
                />
              </View>
              <TextInput
                editable={false}
                style={styles.inputArea}
                placeholder={ClientEmail}
                required={true}
                autoCapitalize="none"
                placeholderTextColor={Colors.productGrey}
                keyboardType="email-address"
                errorMessage="Please enter a valid email address."
                initialValue=""
              />
              {/* <View style={styles.inputArea}> */}
              <TextInput
                editable={false}
                style={{ width: 250 }}
                placeholder={PhoneNumber}
                style={styles.inputArea}
                autoCapitalize="none"
                required={true}
                placeholderTextColor={Colors.productGrey}
                //minLength={6}
                //value={phoneNo}
                //onChangeText={(value) => setPhoneNo(value)}
                initialValue=""
              />
              {/* </View> */}
            </View>
        

            <View
              style={{
                //height: "30%",
                paddingTop: 20,

                flexDirection: "row",
                justifyContent: "center",

                //bottom: 10,
              }}
            >
             
              <View
                style={{
                  width: "30%",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                <Image
                  source={require("../assets/remain.png")}
                  style={{
                    width: 50,
                    height: 50,
                  }}
                />
                {RemainingInvoices=="-1"?<Text
                  style={{
                    color: Colors.darkRedColor,
                    fontWeight: "bold",

                    fontSize: 14,
                    marginTop: 5,
                  }}
                >
                  UNLIMITED
                </Text>:
                <Text
                  style={{
                    color: Colors.darkRedColor,
                    fontWeight: "bold",

                    fontSize: 20,
                    marginTop: 5,
                  }}
                >
                  {RemainingInvoices}
                </Text>}
                <Text
                  style={{
                    color: Colors.productGrey,
                    fontWeight: "bold",
                    fontSize: 11,
                  }}
                >
                  Remaining Invoices
                </Text>
              </View>

              <View
                style={{
                  width: "30%",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                <Image
                  source={require("../assets/pending.png")}
                  style={{
                    width: 50,
                    height: 50,
                  }}
                />
                <Text
                  style={{
                    color: Colors.darkRedColor,
                    fontWeight: "bold",
                    fontSize: 14,
                    marginTop: 5,
                  }}
                >
                  {UsedInvoices}
                </Text>
                <Text
                  style={{
                    color: Colors.productGrey,
                    fontWeight: "bold",
                    fontSize: 11,
                  }}
                >
                  Used Invoices
                </Text>
              </View>
            </View>

            <View style={{ height: "17%", paddingTop: 20 }}>
              <TouchableOpacity
                onPress={() => setModalVisible(true)}
                style={{
                  height: 30,
                  width: "60%",
                  backgroundColor: "#E2E2E2",
                  alignItems: "center",
                  justifyContent: "center",
                  borderRadius: 20,
                  alignSelf: "center",
                }}
              >
                <Text
                  style={{
                    color: "black",
            fontWeight: "bold",
            textAlign: "center",
            fontSize: 14,
                  }}
                >
                  CHANGE PASSWORD
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                onPress={UpdateProfile}
                style={{
                  height: 30,
                  width: "60%",
                  backgroundColor: Colors.themeColor,
                  alignItems: "center",
                  justifyContent: "center",
                  borderRadius: 20,
                  marginTop: 10,
                  marginBottom:25,
                  alignSelf: "center",
                }}
              >
                <Text
                  style={{
                    color: "white",
                    fontWeight: "bold",
                    // letterSpacing: 1,
                textAlign:'center',
                fontSize:16


                  }}
                >
                  UPDATE
                </Text>
              </TouchableOpacity>
            </View>
          </View>
         
      </ScrollView>
      </KeyboardAvoidingView>
      </View>

      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => {
          setModalVisible(!modalVisible);

          // Alert.alert("Modal has been closed.");
        }}
      >
        <View style={styles.centeredView}>
          <View style={styles.modalView}>
          <Card style={{borderRadius:10,width:320,height:380,alignItems:'center',backgroundColor:"white"}}>

      
          <View style={{paddingTop:40}}>
          <Text
              style={{
                fontSize: 18,
                fontWeight: "bold",
                color: "black",
                letterSpacing: 1,
              }}
            >
              CHANGE PASSWORD
            </Text>
          </View>
          <View style={styles.name_inputArea}>
          <TextInput
              style={{width:"95%"}}
              placeholder="Enter Old Password"
              secureTextEntry={oldSecurePass}
              autoCapitalize="none"
              // textContentType='emailAddress'
              placeholderTextColor={Colors.textGreyColor}
              value={oldPass}
              onChangeText={(value) => setOldPass(value)}
              initialValue=""
            />
          <View style={{alignSelf:"center",}}>
          <Icon active name={oldSecurePass?'eye':"eye-off"} color= {Colors.textGreyColor} size={25} 
               onPress = {() => {
             
                if(oldSecurePass == true){
               setOldSecurePass(false)
                }
                else{
                  setOldSecurePass(true)
                }
              }
              }
               />
            </View>
             </View>

             <View style={styles.name_inputArea}>
            <TextInput
              style={{width:"95%"}}

              placeholder="Enter New Password"
              secureTextEntry={securePass}
              autoCapitalize="none"
              //autoCapitalize="words"
              // textContentType='emailAddress'
              placeholderTextColor={Colors.textGreyColor}
              value={newPass}
              onChangeText={(value) => setNewPass(value)}
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

             <View style={styles.name_inputArea}>

            <TextInput
              style={{width:"95%"}}
              
              placeholder="Re-Enter Password"
              autoCapitalize="none"
              secureTextEntry={secureConfirmPass}

              // textContentType='emailAddress'
              placeholderTextColor={Colors.textGreyColor}
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


            <TouchableOpacity
              style={{
                backgroundColor: Colors.themeColor,
                marginTop: 20,
                width: 230,
                height: 40,
                alignItems: "center",
                justifyContent: "center",
                borderRadius: 30,
              }}
              onPress={() => {
                
                change_Password();
              }}
            >
              <Text
                style={{
                  color: "white",
                  fontWeight: "bold",
                  letterSpacing: 1,
                  textAlign:'center',
                fontSize: 16,

                }}
              >
                CONFIRM
              </Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={{
                borderColor: Colors.themeColor,
                borderWidth: 1,
                marginTop: 10,
                width: 230,
                height: 40,
                alignItems: "center",
                justifyContent: "center",
                borderRadius: 30,
              }}
              onPress={() => {
                setModalVisible(!modalVisible);
              }}
            >
                
                  
              <Text style={{ color: Colors.themeColor,fontSize: 16,textAlign:'center', }}>Cancel</Text>
            </TouchableOpacity>
            </Card>
          </View>
        {/* </View>
        </View> */}
        </View>
      </Modal>

     
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
  name1_inputArea: {
    height: 40,
    width: 135,
    marginVertical: 10,

    backgroundColor: "#E2E2E2",
    borderRadius: 25,
    paddingHorizontal: 30,
  },
  name2_inputArea: {
    marginLeft: 20,
    marginVertical: 10,
    height: 40,
    width: 135,
    backgroundColor: "#E2E2E2",
    borderRadius: 25,
    paddingHorizontal: 30,
  },
  inputArea: {
    marginVertical: 5,
    alignSelf: "center",
    height: 40,
    width: 290,
    backgroundColor: "#E2E2E2",
    borderRadius: 25,
    paddingHorizontal: 30,
    flexDirection: "row",
  },
  name_inputArea:{
    marginVertical:4,
    // textAlign:'right',
    height: 40, 
    width:250,
     backgroundColor: '#F2F1F3',
    borderRadius:25,
    paddingHorizontal:30,
    flexDirection:'row',
    marginTop:10
    
    //padding:40,
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
  avatar: {
    width: 120,
    height: 120,
    borderRadius: 63,
    borderWidth: 4,
    borderColor: "white",
    marginBottom: 10,
    alignSelf: "center",
    position: "absolute",
    marginTop: 90,
  },
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    // marginTop: 60,
    

  },
  modalView: {
    margin: 20,
    // height:"100%",
    height:'100%',
    width:"100%",
    backgroundColor: 'rgba(0,0,0,0.3)',
   // borderRadius: 20,
    padding: 35,
    alignItems: "center",
    justifyContent:'center',
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2
    },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5
  },
});

export default Profile;
