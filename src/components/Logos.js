import React from 'react'
import {
    StyleSheet,
    View,
    Text,
    Image,
    ImageBackground
  } from 'react-native';
  import Colors from '../ColorCodes/Colors';

  
function Logos() {
    return (
        <View style={styles.container}>
             <ImageBackground
      source={require('../assets/Splash.jpg')} 
      style={ {width: 130, height: 130,} }
      >
     
        <Text style={styles.logotext}>
            Welcome to my app!
        </Text>
        </ImageBackground>
        </View>
    )
}

const styles = StyleSheet.create({

    container:{
      
      flexGrow:1,
      justifyContent: 'center',
      alignItems:'center',
       backgroundColor:Colors.accentColor,
      paddingTop:10,
    },
    logotext:{
        marginVertical:15,
        fontSize:24,
        color:'rgba(255,255,255, 0.7)',
    }
  });

export default Logos
