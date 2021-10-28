import React from 'react'
import { View, Text, StyleSheet, ScrollView } from 'react-native';
// import { HeaderButtons, Item } from 'react-navigation-header-buttons';

// import HeaderButton from '../components/HeaderButton';

function TermConditionScreen() {
    return (
      <View style={styles.container}>

        <ScrollView>
        <View style={styles.screen}>
            {/* <Text style={styles.heading}>
            Terms and conditions
            </Text> */}
            </View>

            <Text style={styles.smallHeading}>
             Terms and conditions
            </Text>

            <Text style={styles.text}>
            These terms and conditions ("Agreement") set forth the general terms and conditions of your use of the orddel.co.uk website ("Website"), "ORDDEL" mobile application ("Mobile Application") and any of their related products and services (collectively, "Services"). This Agreement is legally binding between you ("User", "you" or "your") and this Website operator and Mobile Application developer ("Operator", "we", "us" or "our"). By accessing and using the Services, you acknowledge that you have read, understood, and agree to be bound by the terms of this Agreement. If you are entering into this Agreement on behalf of a business or other legal entity, you represent that you have the authority to bind such entity to this Agreement, in which case the terms "User", "you" or “your" shall refer to such entity. If you do not have such authority, or if you do not agree with the terms of this Agreement, you must not accept this Agreement and may not access and use the Services. You acknowledge that this Agreement is a contract between you and the Operator, even though it is electronic and is not physically signed by you, and it governs your use of the Services.
            </Text>

            <Text style={styles.smallHeading}>
            Accounts and membership
            </Text>

            <Text style={styles.text}>
            If you create an account on the Services, you are responsible for maintaining the security of your account and you are fully responsible for all activities that occur under the account and any other actions taken in connection with it. We may monitor and review new accounts before you may sign in and start using the Services. Providing false contact information of any kind may result in the termination of your account. You must immediately notify us of any unauthorized uses of your account or any other breaches of security. We will not be liable for any acts or omissions by you, including any damages of any kind incurred as a result of such acts or omissions. We may suspend, disable, or delete your account (or any part thereof) if we determine that you have violated any provision of this Agreement or that your conduct or content would tend to damage our reputation and goodwill. If we delete your account for the foregoing reasons, you may not re-register for our Services. We may block your email address and Internet protocol address to prevent further registration. 
            </Text>

            <Text style={styles.smallHeading}>
            Dispute Resolution
            </Text>

            <Text style={styles.text}>
            The formation, interpretation, and performance of this Agreement and any disputes arising out of it shall be governed by the substantive and procedural laws of the United Kingdom without regard to its rules on conflicts or choice of law and, to the extent applicable, the laws of the United Kingdom. The exclusive jurisdiction and venue for actions related to the subject matter hereof shall be the courts located in the United Kingdom, and you hereby submit to the personal jurisdiction of such courts. You hereby waive any right to a jury trial in any proceeding arising out of or related to this Agreement. The United Nations Convention on Contracts for the International Sale of Goods does not apply to this Agreement. 
            </Text>

            <Text style={styles.smallHeading}>
            Changes and Amendments
            </Text>

            <Text style={styles.text}>
            We reserve the right to modify this Agreement or its terms relating to the Services at any time, effective upon posting of an updated version of this Agreement on the Services. When we do, we will revise the updated date at the bottom of this page. Continued use of the Services after any such changes shall constitute your consent to such changes. 
            </Text>

            <Text style={styles.smallHeading}>
            Acceptance of these Terms
            </Text>

            <Text style={styles.text}>
            You acknowledge that you have read this Agreement and agree to all its terms and conditions. By accessing and using the Services you agree to be bound by this Agreement. If you do not agree to abide by the terms of this Agreement, you are not authorized to access or use the Services. This terms and conditions policy was created with the terms and conditions generator. 
            </Text>
            <Text style={styles.smallHeading}>
            Contacting Us
            </Text>

            <Text style={{...styles.text,paddingBottom:20}}>
            If you would like to contact us to understand more about this Agreement or wish to contact us concerning any matter relating to it, you may do so via the contact form or send an email to info@orddel.co.uk.
This document was last updated on March 31, 2021.
 
            </Text>

            </ScrollView>
        </View>
    )
}

// TermConditionScreen.navigationOptions = navData => {
//     return {
//       headerTitle: 'TERMS & CONDITIONS',
//       headerLeft: ()=>null
//     };
//   };

const styles=StyleSheet.create({

  container:{
    flex: 1,
  },

  screen:{
    alignItems:'center',
},

heading:{
  marginTop:10,
  fontWeight:'bold',
  fontSize:30,
  color:"#EE0202",
},

smallHeading:{
  marginTop:30,
  fontWeight:'bold',
  fontSize:20,
  paddingLeft:18,
  justifyContent:'center',

},

text:{
  marginTop:0,
//   fontFamily:'open-sans-bold',
    // fontWeight:'bold',
    justifyContent:'center',
    textAlign:'justify',
  fontSize:14,
  padding: 20,
  paddingTop:10,
  paddingBottom:0
},

})

export default TermConditionScreen