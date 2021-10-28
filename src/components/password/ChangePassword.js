
import React,{useState}from 'react';
import { StyleSheet , ScrollView} from 'react-native'
import { Container, Header, Picker,Input,Card,CardItem ,Textarea, Form,Right,Tab, Tabs, Button,Item, Content, Text,View } from 'native-base'
import { Icon } from 'react-native-elements'




const ChangePassword = ({route}) =>{


  const { Login , Password } = route.params

 
  const [data , setData] = useState(Login.toString())
  const [existingPass , setExistingPass] = useState("") 
  const [newPass , setNewPass] = useState("") 
  const [c_NewPass , setC_NewPass] = useState("")     


  const updatePassword = () => {
    
    if(existingPass == Password[0]){

    const res = fetch('http://110.37.207.41:8069/update_shipment', {
     method: 'POST',
     headers: {
       Accept: 'application/json',
       'Content-Type': 'application/json'
     },
     body:JSON.stringify({
      "jsonrpc": "2.0",
      "params":{
      "login":data,
      "password":newPass, 
      "confirmpass":c_NewPass,
      }
    })
   
      
   }).then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
    console.log("shaheefr")
  })
}else{
  alert("Incorrect password")
}
   
   }
  return (
    <ScrollView>
    <Container style = {{backgroundColor:'#f7f7f7'}}>
   
    <Content style={{padding:10}}>

     
    <View style = {{flexDirection:'row',alignItems:'center',justifyContent:'space-between'}}>
            
    <View style = {{flexDirection:'row',alignItems:'center',justifyContent:'space-between',marginTop:10}}>
            
            <Item regular  style = {{borderRadius:30,backgroundColor:'#ededed',borderColor:'#ededed'}}>
            <Input placeholder = "Existing password"
            value={existingPass}
            onChangeText={text => setExistingPass(text)}
            />
          </Item>
          </View>
          </View>

          <View style = {{flexDirection:'row',alignItems:'center',justifyContent:'space-between',marginTop:10}}>
            
            <Item regular  style = {{borderRadius:30,backgroundColor:'#ededed',borderColor:'#ededed'}}>
            <Input placeholder = "New Password"
            value={newPass}
            onChangeText={text => setNewPass(text)}
            />
          </Item>
          </View>

          <View style = {{flexDirection:'row',alignItems:'center',justifyContent:'space-between',marginTop:10}}>
            
            <Item regular  style = {{borderRadius:30,backgroundColor:'#ededed',borderColor:'#ededed'}}>
            <Input placeholder = "Confirm new password"
            value={c_NewPass}
            onChangeText={text => setC_NewPass(text)}
            />
          </Item>
          </View>


          <View style = {{marginTop:10,flexDirection:'row',width:'100%',justifyContent:'space-around',marginTop:10}}>
        <Card style = {{width:150,alignItems:'center',backgroundColor:'#0f70b7',borderRadius:30}}>
            <CardItem
            button onPress = {updatePassword}
            style = {{backgroundColor:'#0f70b7'}}>
              
              <Text style = {{color:'white'}}>Save</Text>
            
             </CardItem>
           </Card>
           </View>
            </Content>

         

  </Container>
  </ScrollView>
  );
};

const styles = StyleSheet.create({
 
});


export default ChangePassword