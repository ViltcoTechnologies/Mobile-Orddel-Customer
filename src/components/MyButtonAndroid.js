import React from 'react'
import { Text, StyleSheet, TouchableNativeFeedback, View, TouchableOpacity, Platform} from 'react-native';
import Colors from '../ColorCodes/Colors';
// import Colors from '../Constants/Colors';


function My_Buttons(props) {

    let ButtonComponent=TouchableOpacity;
    if(Platform.Version>=21){
        ButtonComponent=TouchableNativeFeedback;
    }

    return (
        <View style={styles.buttonContainer}>
        <ButtonComponent activeOpacity={0.8} onPress={props.onPress} >
        <View style={styles.button}>
            <Text style={styles.buttonText}>
                {props.children}
            </Text>
        </View>
        </ButtonComponent>
        </View>
    )
}

const styles=StyleSheet.create({
    button:{
        backgroundColor:'white',
        paddingVertical:12,
        paddingHorizontal:60,
        borderRadius:25,
        marginTop: 50,
        // width:20,
        // height:40,
        
    },
    buttonContainer:{
        // width:5,
        // height:100,
        borderRadius:10,
        // overflow:'hidden'

    },
    buttonText:{
        color: Colors.darkRedColor,
        //fontFamily:'',
        //fontStyle:'italic',
        fontSize:17,
        fontWeight:'bold',
        // justifyContent:'center',
        // alignItems:'center'
    }

})

export default My_Buttons