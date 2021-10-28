import {useEffect} from 'react'

export default () => {

const ShipmentBooking = () => {
 console.log("Api Call")

    fetch('http://110.37.207.41:8069/shipper_booking/', {
  method: 'POST',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    load_type: 'container',
    origin_city: '',
    destination_city: '',
    delivery_option: '',
    cargo_type: '',
    cargo_amount: '',
    cargo_product_type: '',
    cargo_packing_list: '',
    payment_type: ''
  })
});


}

useEffect(() => {
    ShipmentBooking();
    
}, [])

}