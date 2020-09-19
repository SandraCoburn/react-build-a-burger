import axios from "axios";
const instance = axios.create({
  baseURL: "https://react-build-my-burger.firebaseio.com/",
});
export default instance;
