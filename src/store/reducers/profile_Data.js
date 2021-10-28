import React,{useState, useEffect} from 'react';
import { View, Text, StyleSheet, FlatList, SafeAreaView, ActivityIndicator } from 'react-native';
// import {MEALS, CATEGORIES} from '../../data/dummy-data';
import { SET_RECORD } from '../actions/profile_Data';
// import {CATEGORY_ID, CLEAR, CATID_UPDATE} from '../actions/meals';
//import {useEffect} from 'react';


const initialState={
   data:[],
   id:0,
   Company_Name:"",
   Company_NTN:"",
   phone:"",
   NTN_No:"",
   token:"",
   Company_Head_Office_adrs:"",
   login:"",
   password:"",
   confirmPass:"",
   Rate:false,
   Type:false,
   Delivery_Time:false,
   Rate_Truck:false,
   Id:"",
   Driver_info:false,
   Origin_City:"",
   Destination_City:"",
   price_per_lane:0.0,
   price_per_ton:0.0
 
};

// useEffect(() => {
//   fetch('http://food.theflashdemo.com/api/all_meal')
//     .then((response) => response.json())
//     .then((json) => {
//       initialState.meals=json.Meals
//       console.log("initialState.meals",initialState.meals)
//       // setTitle(json.name)
//       // setDescription(json.image);
//     })
//     .catch((error) => console.error(error))
    // .finally(() => setLoading(false));
// }, []);

const profile_Data = (state = initialState, action) => {
    switch (action.type) {
      case SET_RECORD:
          const new_response=action.response;
          state.data=action.response;
          console.log("From Reducer Response:",new_response);
        //   console.log("From Reducer Response:",new_response.Company_NTN);
        //   state.id=new_response.id;
        //   console.log("state.id:",state.id);
        //   state.Company_Name=new_response.Company_Name;
        //   console.log("state.Company_Name:",state.Company_Name);
    //   return (
        // <FlatList
        // data={new_response}
        // keyExtractor={({ id }, index) => id}
        // renderItem={({ item }) => {
        //   console.log("item.id",item.id)
        //   console.log("item.Company_Name",item.Company_Name)
        //   // loadedProducts.push(
        //     // new Category(
        //     //   item.id,
        //     //   item.title,
        //     //   item.imageUrl,
        //     //   // resData[key].price
        //     // ))
        // }}
        // />
        // meals: action.meals,
        // userProducts: action.meals.filter(catId => catId.id === 'c1')
    //   );

          
      default:
        return state;
    }
  };

export default profile_Data;