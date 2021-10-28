
import React,{Component }from 'react';
import { StyleSheet , ScrollView} from 'react-native'
import { Container, Header, Picker,Input,Card,CardItem ,Textarea, Form,Right,Tab, Tabs, Button,Item, Content, Text,View } from 'native-base'
import { Icon } from 'react-native-elements'




export default class Help extends Component{

    
      

render(){
  return (
    <ScrollView>
   
   
    

     
    <View style = {{alignItems:'center',justifyContent:'space-between',padding:10}}>
            
           
            <Textarea rowSpan={15} style={{width:'100%',backgroundColor:'white'}} bordered placeholder = "Enter your query" />
          
         

         
          
          <Card style = {{marginTop:'5%',width:'100%'}}>
            <CardItem
            button
            style = {{backgroundColor:'#0f70b7',justifyContent:'center'}}>
              
              <Text style = {{color:'white'}}>SEND</Text>
            
             </CardItem>
           </Card>
           
            </View>
        <View style ={{justifyContent:'center',alignItems:"center"}}>
            <Text style = {{color:'gray'}}>Version 1.0</Text>
            <View style ={{justifyContent:'center',alignItems:"center"}}>
            <Button transparent><Text>Privacy Policy</Text></Button>
            </View>
        </View>

  
  </ScrollView>
  );
}};

const styles = StyleSheet.create({
 
});


