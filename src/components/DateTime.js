import React, { useState, useEffect } from "react";
import {
  StyleSheet,
  View,
  ImageBackground,
  TouchableOpacity,
  Image,
  ScrollView,
  LogBox,
  FlatList,
  StatusBar,
  SafeAreaView,
  Animated,
  TextInput,
  Platform,
  BackHandler,
  KeyboardAvoidingView,
  Alert,
  Modal,
  Pressable
} from "react-native";
import {
  Container,
  CardItem,
  Header,
  Content,
  Left,
  Footer,
  Body,
  Right,
  Button,
  Title,
  Text,
  DatePicker,
  Item,
  Input,
  Spinner,
} from "native-base";
// import { Icon } from 'react-native-elements';
//import DateTimePicker from "@react-native-community/datetimepicker";
import DateTimePicker from '@react-native-community/datetimepicker';
function DateTime({ navigation ,route }) {

      const [date, setDate] = useState(new Date(1598051730000));
      const [mode, setMode] = useState('date');
      const [show, setShow] = useState(false);
    
      const onChange = (event, selectedDate) => {
        const currentDate = selectedDate || date;
        setShow(Platform.OS === 'ios');
        setDate(currentDate);
      };
    
      const showMode = (currentMode) => {
        setShow(true);
        setMode(currentMode);
      };
    
      const showDatepicker = () => {
        showMode('date');
      };
    
      const showTimepicker = () => {
        showMode('time');
      };



return(

    <View style={{ flex:1, justifyContent:'center',  }}>
      <View style={{  backgroundColor:'red', }} >
        <Button onPress={showDatepicker} title="Show date picker!" />
      </View>
      <View style={{  backgroundColor:'red' }}>
        <Button onPress={showTimepicker} title="Show time picker!" />
      </View>
      {show && (
        <DateTimePicker
          testID="dateTimePicker"
          value={date}
          mode={mode}
          is24Hour={true}
          display="default"
          onChange={onChange}
        />
      )}
    </View>
)
}

export default DateTime;