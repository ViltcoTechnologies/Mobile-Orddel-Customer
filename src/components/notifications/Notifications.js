import React, { useState , useEffect } from 'react';
import { Image , ScrollView , FlatList,View } from 'react-native';
import { Container, Spinner, Content, Card, CardItem, Thumbnail, Text, Button, Left, Body, Right } from 'native-base';
import { Icon } from 'react-native-elements'
const Notifications = ({navigation , route}) => 
{

  const { Shipper_ID } = route.params
  

  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);
 
  
   console.log(Shipper_ID)
  useEffect(() => {
    fetch('http://110.37.207.41:8069/shipper/Return/ShipperList?shipper_id='+Shipper_ID)
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error(error))
      .finally(() => setLoading(false));

      
  }, []);

    return (
      <ScrollView style = {{flex:1,padding:5}}>
{data.length == 0?
     <View style = {{justifyContent:'center',alignItems:'center',marginTop:'30%'}}> 
     <Icon active name='info' color= "#0f70b7" size={200}/>
     <Text style = {{color:'#0f70b7',fontWeight:'bold',fontSize:25}}>NO RECORD</Text>
     </View>
     : null }
{isLoading ? <Spinner color='#0f70b7' /> : (
        <FlatList
          data={data}
          keyExtractor={({ id }, index) => id.toString()}
          renderItem={({ item }) => (   
      <Container style={{height:"15%"}}>
       
       
        <Content>
          <Card>
            <CardItem
            
            > 
              <Left>
                <Thumbnail source={{uri: 'https://picsum.photos/200/300'}} />
                <Body>
                   <Text style = {{ color :'#0f70b7'}}>{item.shipper_name}</Text>
                  <Text note>{item.booking_status}</Text>
                </Body>
              </Left>
            </CardItem>
           
            <CardItem>

              <Left>
              <Card>
            <CardItem
          
            >
              
              <Right>
              
              </Right>
             </CardItem>
           </Card>
              </Left>

              <Body  style = {{flexDirection:'row'}}>
                
                
                </Body>
              <Right>
              <Card>
            <CardItem
              button
              onPress = { () => navigation.navigate("PaymentSlip")}
            >
              <Icon active name="payment" color = 'darkred' size={25}/>
              <Right>
              
              </Right>
             </CardItem>
           </Card>
              </Right>
            </CardItem>
          </Card>
        </Content>


         
      

      </Container>

)}
/>
)}
      </ScrollView>
    );
  
}

export default Notifications