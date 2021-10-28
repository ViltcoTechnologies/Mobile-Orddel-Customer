import React, { useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Platform,
} from "react-native";
import Ionicons from "react-native-vector-icons/Ionicons";
import FontAwesome from "react-native-vector-icons/FontAwesome";
import Colors from "../ColorCodes/Colors";

const OrderCartItem = (props) => {
  const MyIcon1 = <FontAwesome name="minus" size={15} color="#EE0202" solid />;
  const MyIcon2 = <FontAwesome name="plus" size={15} color="#EE0202" solid />;

  //const mealId = useSelector(state => state.cart.items.id);

  //const availableMeals=useSelector(state=>state.mealReducer.selectedMeal);
  //const availableMeals=useSelector(state=>state.selectedMeal);
  //console.log(availableMeals,'  selected')
  //const selectedMeal = MEALS.find(meal => meal.id === mealId);
  //const dispatch = useDispatch();
  //const mealId = props.navigation.getParam('mealId');
  //console.log(mealId,"  mealID  ")

  return (
    <View
      style={{
        flexDirection: "row",
        borderBottomWidth: 0.5,
        borderBottomColor: "grey",
        marginTop: 10,
        width: "100%",
      }}
    >
      {/* <TouchableOpacity
            onPress={props.onDelete}
            // style={styles.deleteButton}
          >
            <Ionicons
              name={Platform.OS === 'android' ? 'md-trash' : 'ios-trash'}
              size={23}
              color="#EE0202"
            />
          </TouchableOpacity> */}
      <View style={{ width: "30%", justifyContent: "center" }}>
        <Text
          style={{
            marginLeft: 5,
            color: Colors.productGrey,
            textAlign: "left",
          }}
        >
          {props.name}
        </Text>
      </View>
      <View style={{ width: "20%", justifyContent: "center" }}>
        <Text style={{ color: Colors.productGrey, textAlign: "center" }}>
          {props.unit}
        </Text>
      </View>
      <View style={{ width: "20%", justifyContent: "center" }}>
        <Text style={{ color: Colors.productGrey, textAlign: "center" }}>
          {props.quantity}
        </Text>
      </View>

      <View style={{ width: "20%", justifyContent: "center" }}>
        <Text style={{ color: Colors.textGreyColor, textAlign: "right" }}>
          £ {props.price.toFixed(2)}
        </Text>
      </View>

      {/* {props.addable && ( */}
      {/* <TouchableOpacity
        onPress={props.onDelete}
        style={{ alignItems: "center", justifyContent: "center" }}
        // style={styles.deleteButton}
      >
        <Ionicons
          name={Platform.OS === "android" ? "md-trash" : "ios-trash"}
          size={25}
          color="#EE0202"
        />
      </TouchableOpacity> */}
      {/* )}  */}
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
    marginTop: 12,
    padding: 10,
    backgroundColor: "white",
    borderWidth: 0.5,
    borderColor: "#EE0202",
    flexDirection: "row",
    justifyContent: "space-between",
    marginHorizontal: 20,
    borderRadius: 15,
  },
  itemData: {
    flexDirection: "row",
    alignItems: "center",
  },
  quantity: {
    color: "#EE0202",
    fontWeight: "bold",
    fontSize: 18,
    marginRight: 4,
  },

  title: {
    fontFamily: "open-sans-bold",
    fontSize: 16,
    color: "orange",
    fontWeight: "bold",
  },

  rupees: {
    color: "black",
    //fontFamily: 'open-sans-bold',
    fontSize: 16,
  },

  deleteButton: {
    marginLeft: 10,
  },

  button: {
    marginLeft: 15,
  },
});

export default OrderCartItem;
