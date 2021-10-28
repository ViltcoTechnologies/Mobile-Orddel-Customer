import { StyleSheet } from "react-native";
import Colors from "../src/ColorCodes/Colors";
export default StyleSheet.create({
  image: {
    //    height:"100%",
    //    width:"100%" ,
    flex: 1,
  },
  logo: {
    height: "20%",
    opacity: 0.5,
    justifyContent: "center",
    alignItems: "center",
  },
  topContainer: {
    marginTop: "30%",
    height: "50%",
    // alignSelf:'center',
  },
  buttonContainer: {
    flexDirection: "column",

    height: "60%",
    //  justifyContent:'flex-end',
    //alignItems:'center',
  },

  submitButton: {
    height: 50,
    width: "70%",
    alignSelf: "center",
    justifyContent: "center",

    // marginBottom:10,
    borderRadius: 30,
  },
  secondSubmitButton: {
    height: 50,
    width: "70%",
    alignSelf: "center",
    justifyContent: "center",
    marginTop: 10,
    borderRadius: 30,
    borderColor: Colors.darkRedColor,
  },
  buttonView: {
    // marginTop:30,
    alignItems: "center",
    //paddingBottom:10
  },

  button: {
    justifyContent: "center",
    alignItems: "center",
    marginHorizontal: 10,
    width: "70%",
    height: 40,
    backgroundColor: Colors.darkRedColor,
    borderRadius: 25,
  },

  buttonText: {
    color: "#ffffff",
    fontWeight: "bold",
    fontSize: 20,
  },
  // buttonText:{
  //     color:'#0f70b7'
  // },
  tinyLogo: {
    marginTop: "10%",
    width: 200,
    height: 200,
  },
});
