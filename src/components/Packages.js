import React,{useEffect,useState} from 'react';
import URL from '../api/ApiURL';
import {View,Text,Image,ImageBackground,TouchableOpacity, StyleSheet,ScrollView,FlatList,LogBox,BackHandler} from 'react-native';
import Card from '../components/Card';
import {
    Container,
    Header,
    Spinner,
} from "native-base";
import FontAwesome from 'react-native-vector-icons/FontAwesome';
import Colors from '../ColorCodes/Colors';
import { useRoute, useFocusEffect } from "@react-navigation/native";
function Packages({navigation,route}) {

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




    const [packageData,setPackageData]=useState("");
    const [imagePackage,setImagePackage]=useState("");
    const [loading,setLoading]=useState(false);
    useEffect(() => {
    LogBox.ignoreLogs(['Failed child context type']);

        setLoading(true);
        fetch(URL+'/client_app/list_packages/')
        // fetch(URL+'/client_app/clients_list/33/')
        .then((response) => response.json())
        .then((responseJson) => {
            
              console.log("Packages:",responseJson);
              setPackageData(responseJson.all_package);
            setLoading(false);

            //   console.log("Dashboard:",responseJson.client_dashboard.client_name);
              //console.log("Buisness Detail:",responseJson.client_businesses[0]['name']);
            // if (json["response"] == "Record does not exist or not found") {
            //   setLoading(true);
            // } else {
            //   dispatch(ApiDataAction.SetListData(responseJson)); 
            //   dataa=responseJson;
            //   setData(responseJson);
            //   //console.log(json);
            
            // }
          })
          .catch((error) => console.error(error))
    }, [])





    return (
       <View style={{flex:1,height:"100%",justifyContent:'space-around'}}>
           
           {loading ? (
        <Spinner color={Colors.themeColor} size={50} />
        
      ) :
           <FlatList
            data={packageData}
            keyExtractor={item => item.id}
            style={{width:'100%'}}
            renderItem={itemData => (
                <TouchableOpacity onPress={()=>navigation.navigate("PaymentMethods",{id:itemData.item.id})} style={{width:'90%',alignSelf:'center',marginTop:10,bottom:5}}>
                <ImageBackground
   
                        source={itemData.item.name=="Starter" ?require(`../assets/Starter.jpg`):itemData.item.name=="Green" ?require(`../assets/Green.jpg`):itemData.item.name=="Gold" ?require(`../assets/Gold.png`):itemData.item.name=="Platinum" ?require(`../assets/Platinum.png`):null}        
                        style={{ width: "100%", height:130}}
                        >
                         <View style={{height:"100%"}}>
                             <View style={{height:"48%",width:'75%',justifyContent:'center'}}>
                                
                                 <Text style={{color:'white',fontSize:18,textAlign:'center',fontWeight:'500',letterSpacing:1}}>{itemData.item.name.toUpperCase()}</Text>
         
                                 
                             </View>
                             <View style={{height:"53%",width:"100%",flexDirection:'row'}}>
                                 <View style={{width:"50%",justifyContent:'center'}}>
                                 {itemData.item.no_of_invoices=="-1"?<Text style={{color:'white',fontSize:17,textAlign:'center'}}>UNLIMITED</Text>:<Text style={{color:'white',fontSize:24,textAlign:'center'}}>{itemData.item.no_of_invoices}</Text>}
                                     
                                     <Text style={{color:'white',fontSize:10,textAlign:'center'}}>INVOICES</Text>
         
                                 </View>
                                 <View style={{width:"50%",justifyContent:'center'}}>
                                     <View style={{flexDirection:'row',justifyContent:'center'}}>
                                     <Text style={{color:'white',fontSize:24,textAlign:'center'}}>{itemData.item.price}</Text>
                                     <Text style={{color:'white',fontSize:14,paddingTop:10,paddingLeft:2}}>£</Text>
                                     </View>
                                     <Text style={{color:'white',fontSize:10,textAlign:'center'}}>PRICE</Text>
                                     
                                 </View>
                             </View>
                            
                         </View>
                            
         
                        </ImageBackground>
                
                </TouchableOpacity>
            )}
        />
            }
        


       




       
       </View>
    )
}


const styles = StyleSheet.create({
    cartItem: {
      flex: 1,
      marginTop:12,
      padding: 10,
      backgroundColor: 'white',
      borderWidth: .5,
      borderColor: "#EE0202",
      flexDirection: 'row',
      justifyContent: 'space-between',
      marginHorizontal: 20,
      borderRadius:15
    },
})

export default Packages