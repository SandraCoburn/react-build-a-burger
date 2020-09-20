import React, { Component } from "react";
import axios from "../../axios.orders";

import Order from "../../components/Order/Order";
import withErrorHandler from "../../hoc/withErrorHandler/withErrorHandler"; //wrap component to handle errors

class Orders extends Component {
  state = {
    orders: [],
    loading: true,
  };
  componentDidMount() {
    axios
      .get("/orders.json")
      .then((res) => {
        //Firebase returns an object as a response, to turn it into array:
        const fetchedOrders = [];
        for (let key in res.data) {
          fetchedOrders.push({ ...res.data[key], id: key }); //copy of data to get id
        }
        this.setState({ loading: false, orders: fetchedOrders });
      })
      .catch((er) => {
        this.setState({ loading: false });
      });
  }
  render() {
    return (
      <div>
        {this.state.orders.map((order) => (
          <Order
            key={order.id}
            ingredients={order.ingredients}
            price={+order.price}
          />
        ))}
      </div>
    );
  }
}
export default withErrorHandler(Orders, axios);
