import React,{useEffect} from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Platform
} from 'react-native';
import  Ionicons  from 'react-native-vector-icons/Ionicons';
import FontAwesome from 'react-native-vector-icons/FontAwesome';
import Colors from '../ColorCodes/Colors';
// import CurrencyFormatter from "react-native-currency-format";


const InvoiceItem = props => {


 

  return (


    <View style={{flexDirection:'row',borderBottomWidth:0.5,borderBottomColor:'grey',marginTop:10,alignItems:'space-around',width:'100%',marginBottom:1,paddingRight:10}}>

        <View style = {{width:'25%'}}>
            <Text style={{marginLeft:2,color:Colors.productGrey,fontWeight:'bold',textAlign:'left'}}>{props.name}</Text>
        </View>
        {/* <View style = {{width:'20%',alignItems:'center'}}>
        
        <Text style={{color:Colors.productGrey}}>{props.unit}</Text>
        </View> */}
        <View style = {{width:'15%',alignItems:"center"}}>
        
            <Text style={{color:Colors.productGrey}}>{props.quantity}</Text>
        </View>
        
        
        <View style = {{width:'20%'}}>
        
            <Text style={{color:Colors.productGrey,textAlign:'right'}}>£ {parseFloat(props.price).toFixed(2)}</Text>
        </View>
        <View style = {{width:'18%',paddingLeft:"2%"}}>
        
            {props.vat==0?<Text style={{color:Colors.productGrey,textAlign:'right',marginRight:5}}>£ {props.vat}</Text>:<Text style={{color:Colors.productGrey,textAlign:'right',marginRight:5}}>£ {parseFloat(props.vat).toFixed(2)}</Text>}
        </View>
        <View style = {{width:'25%'}}>
        
            <Text style={{color:Colors.productGrey,textAlign:'right',marginRight:5}}>£ {parseFloat(props.amount).toFixed(2)}</Text>
        </View>
        
    </View>




    // <View style={styles.cartItem}>
    //   <View style={styles.itemData}>
    //     <Text style={styles.quantity}>{props.quantity} </Text>
    //     <Text style={styles.title}>{props.name}  </Text>
        
    //   </View>
    //   <View style={styles.itemData}>
    //     <Text style={styles.rupees}> Rs.{props.amount.toFixed(2)}</Text>
        
    //     {props.deletable && (
    //       <TouchableOpacity
    //         onPress={props.onRemove}
    //         style={styles.deleteButton}
    //       >
    //         <Ionicons
    //           name={Platform.OS === 'android' ? 'md-trash' : 'ios-trash'}
    //           size={23}
    //           color="#EE0202"
    //         />
    //         {/* {MyIcon1} */}
    //       </TouchableOpacity>
    //     )}

    //     {/* {props.addable && (
    //       <TouchableOpacity
    //         onPress={props.onAddPress}
    //         style={styles.deleteButton}
    //       >
    //         {MyIcon2}
    //       </TouchableOpacity>
    //     )} */}
        
    //   </View>
    // </View>
  );
};

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
  itemData: {
    flexDirection: 'row',
    alignItems: 'center',
    
  },
  quantity:{
    color: "#EE0202",
    fontWeight:'bold',
    fontSize: 18,
    marginRight: 4,
  },
 
  title: {
    fontFamily: 'open-sans-bold',
    fontSize: 16,
    color:'orange',
    fontWeight:'bold'
  },

  rupees: {

    color:'black',
    //fontFamily: 'open-sans-bold',
    fontSize: 16,
  },

  deleteButton: {
    marginLeft: 20
  },
  
  button: {
    marginLeft:15,
  },
});

export default InvoiceItem;

