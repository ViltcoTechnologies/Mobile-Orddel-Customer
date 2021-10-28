import React, { useState } from "react";  
import { Platform, SafeAreaView,StyleSheet, View,Text,Image, Button, TextInput,TouchableOpacity, ImageBackground,KeyboardAvoidingView,ScrollView} from "react-native";  
import { Card , CardItem ,Right,Input} from 'native-base'
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import { Container, Header, Content,Item , Form , Label ,Spinner } from 'native-base';
import {
  CodeField,
  Cursor,
  useBlurOnFulfill,
  useClearByFocusCell,
} from 'react-native-confirmation-code-field';
import Colors from '../../ColorCodes/Colors';
import URL from '../../api/ApiURL';


 
const CELL_COUNT = 4;



const VerificationCode = ({navigation,route}) => {  

  const { Email , Phone_No,EmailVerify,first_name,last_name,password,riderId,gender,packageId} = route.params 
    
  //const [code_1 , setCode_1] = useState('1')
  //const [code_2 , setCode_2] = useState('2')
  const [code_final , setCode_final] = useState('');
  const [response , setResponse] = useState('');
  const [counter, setCounter] = useState(0);
  const [loading,setLoading]=useState(false);
  const [isLoading,setIsLoading]=useState(false);

 
//Resend Code
const [value, setValue] = useState('');
const ref = useBlurOnFulfill({value, cellCount: CELL_COUNT});
const [props, getCellOnLayoutHandler] = useClearByFocusCell({
  value,
  setValue,
});

const send_Verification_Code = () => {
      
//console.log("ph o",Phone_No);
if(counter!=3)
{
  fetch(URL+'/resend_otp/', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    },

   body : JSON.stringify({

    "phone_number" : Phone_No
  
  
  })
    

    
  }).then((res) => res.json())
  .then((json) => {
    console.log("Resend Response: ",json);
    setCounter(counter + 1);

    if(json!='Verification code resent')
    {
      alert("Please wait, there is request load on our server while sending verification code")
    }
    else{
      alert("Code send successfully");
    }
    
    setResponse(json)
  }).catch((error)=>console.log(error))
}
else {
  alert("Maximum attempts reached");
}
  
} 




  const signup=()=>{
    console.log("package Id:",packageId);
    fetch(URL+'/client_app/client_registration_v2/', {
          method: 'POST',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
          },
          body:JSON.stringify({
          
                first_name: first_name,
                last_name: last_name,
                email: Email,
                phone_number: Phone_No, 
                password: password,
                address: "",
                current_location: "",
                gender: gender,
                image: "",
                package:packageId,
                preferred_delivery_person:riderId,
                otp_status:"True"




         
           
            
           
         })
        
           
        }).then( async (response) => {
         let data = await response.json();
         console.log("signup",data)
         console.log("signup",response.status)
         if(response.status==200){
     setLoading(false);

          navigation.navigate(EmailVerify);

           
         }
        else{
          //  setToastMessage(data.message)
           setIsLoading(false);
     setLoading(false);
           alert(data.message);
         }
 
       })
        .catch ((error)=>
          console.log("Something went wrong", error)
        )
  }

 // console.log(code_final)
  
  const check_Verification_Code = () => {
     console.log(code_final , Phone_No);
     setLoading(true);
    if(code_final!=""){
      const res = fetch(URL+'/verify_otp_v2/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
    
       body : JSON.stringify({
    
  
          "phone_number":Phone_No,
           "verification_code":code_final,
          //  "user_type":"delivery_person"
      })
        
    
        
      }).then( async (response) => {
        let data = await response.json();
       //
       console.log("status code check verification: ",response.status)
        if(response.status==200)
        {
          if(EmailVerify=="ChangeForgotPassword"){
            navigation.navigate(EmailVerify);
            setLoading(false);
          }
          else{
            signup();

          }
          // navigation.navigate("EmailVerification");
  
        }
        else{
          //navigation.navigate("LandingScreen");
     setLoading(false);

          console.log("message",data.message);
          setCode_final("");

          alert(data.message)
        }
        
      })
       .catch ((error)=>
         console.log("Something went wrong", error)
       )
      
    }
    else{
     setLoading(false);

      alert("Please enter code")
    }
    
    
    //setResponse(json)
   
    
    
    //console.log(response["verification_status"])

    //if(response["verification_status"] == "approved"){
      //console.log("shhaeer")
    
   
    //}
    //else{
     // alert("Invalid Code!")
    //}
  
  
  } 
  
  
  
  


return (  

  // <KeyboardAvoidingView style={{ flex: 1 }}
  // behavior={Platform.OS == "ios" ? "padding" : null} >
<View style={styles.container}>  

{/* <ScrollView keyboardShouldPersistTaps="always" showsVerticalScrollIndicator={false}> */}

<View style={styles.header}>
  <ImageBackground
      source={require('../../assets/Splash.jpg')} 
      style={{width: "100%", height: "100%"}}
      >
      <Text style={{color:"white",marginVertical:"5%",
        fontSize:35,alignSelf:"center",marginTop:'15%',borderBottomWidth:2, borderBottomColor:'white',fontWeight:'bold'}}>
            Verification
        </Text>
        
        {/* <Text style={{color:Colors.yellowColor,marginVertical:15,
        fontSize:20,alignSelf:"center",marginTop:10}}>
          Write your Info and register yourself
        </Text> */}
      </ImageBackground>
  </View>
 
  
 
  <View style={styles.footer}>
  <ScrollView>
  <Image source={require('../../assets/verification.png')} 
        style={{ height:80,width:80,alignSelf:'center'}}
          />
    <Text style={{fontSize:17,fontWeight:'bold',padding:20}}>We have sent you an access code via SMS Message for Verification.</Text>
    {/* <View style={styles.g_container}> */}
{/* <Text style = {{alignSelf:'center',marginTop:50,color:'red',fontSize:20,fontWeight:'bold'}}>VERIFICATION</Text> */}

<SafeAreaView style={styles.root}>
      
      <CodeField
        ref={ref}
        {...props}
        value={code_final}
        onChangeText={text => setCode_final(text)}
        cellCount={CELL_COUNT}
        // rootStyle={styles.codeFieldRoot}
        keyboardType="number-pad"
        textContentType="oneTimeCode"
        renderCell={({index, symbol, isFocused}) => (
          <Text
            key={index}
            style={[styles.cell, isFocused && styles.focusCell]}
            onLayout={getCellOnLayoutHandler(index)}>
            {symbol || (isFocused ? <Cursor /> : null)}
          </Text>
        )}
      />
    </SafeAreaView>



{/* <TouchableOpacity
onPress = {send_Verification_Code}
style = {{
  shadowColor: "#000",shadowOffset: {width: 0,height: 2,},shadowOpacity: 0.25,shadowRadius: 5.84,elevation: 5,
  
  
  flexDirection:'row',width:150,height:45,borderRadius:25,justifyContent:'center',alignItems:'center',alignSelf:'center',marginTop:70,borderWidth:1,borderColor:'white',backgroundColor:'white'}}>
  {/* <MaterialIcons active name="replay" color = '#0f70b7' size={25}/> */}

  {/* <Text style = {{color:'#0f70b7',fontSize:18,fontWeight:'bold'}}>Resend</Text> */}
{/* </TouchableOpacity> */} 
     






<TouchableOpacity
 button onPress = {check_Verification_Code}
style = {{
  shadowColor: "#000",shadowOffset: {width: 0,height: 2,},shadowOpacity: 0.25,shadowRadius: 5.84,elevation: 5,
  
  
  flexDirection:'row',width:Platform.OS=='android'?70:90,height:Platform.OS=='android'?70:90,marginTop:Platform.OS=='android'?25:50, borderRadius:Platform.OS=='android'?40:50,justifyContent:'center',alignItems:'center',alignSelf:'center',borderWidth:1,borderColor:Colors.darkRedColor,backgroundColor:Colors.darkRedColor}}>
  

  {/* <Text style = {{color:'white',fontSize:18,fontWeight:'bold'}}>Next</Text> */}
  {loading ? (
              <Spinner color={"white"} />
            ) : (
  <MaterialIcons name="navigate-next" color = 'white' size={Platform.OS=='android'?50:70} />)}
</TouchableOpacity>
<View style={styles.signupContianer}>
      <Text style={styles.signupText}> Didn't receive code?  </Text>
      

        <TouchableOpacity 
         onPress={ send_Verification_Code} >
        <Text style={{color:Colors.darkRedColor,fontWeight:'bold'}}>
         Resend Code
          </Text>
      </TouchableOpacity>
                
    </View>

  </ScrollView>


  {/* </View> */}

</View>
 {/* </ScrollView> */}
  
</View>  
// </KeyboardAvoidingView>
);  

}  

const styles = StyleSheet.create({  

  root: {padding:5},
  title: {textAlign: 'center', fontSize: 30},
  codeFieldRoot: {marginTop: 30},
  cell: {
    width: 50,
    height: 60,
    lineHeight: 38,
    fontSize: 24,
    borderWidth: 2,
    borderColor: Colors.darkRedColor,
    textAlign: 'center',

    
    borderRadius:10,
    color:'black'
  },
  focusCell: {
    borderColor: Colors.darkRedColor,
  },
  container: {  
    flex: 1,  
  
    backgroundColor:'blue'
  
},

  headerText: {  
    fontSize: 20,  
    textAlign: "center",  
    margin: 10,  
    fontWeight: "bold"  ,
   
},  
TextInputStyle: {  
    textAlign: 'center',  
    height: 40,  
    borderRadius: 10,  
    borderWidth: 2,  
    borderColor: '#009688',  
    marginBottom: 10  
}  ,
header: {
  flex: 2,
},

footer: {
  flex: 5,
  width:"100%",
  backgroundColor: '#ffffff',
  // borderTopLeftRadius: 30,
  // borderTopRightRadius: 30,
  // paddingVertical: 10,
  paddingHorizontal:Platform.OS === 'android' ?20:40
   
},
signupContianer:{
  flexGrow: 1,
justifyContent: 'center',
alignItems: 'center',
flexDirection: 'row',
marginTop:80

}
});





export default VerificationCode