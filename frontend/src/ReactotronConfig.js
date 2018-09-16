import Reactotron from 'reactotron-react-js';
import { reactotronRedux } from 'reactotron-redux';

Reactotron.configure({name: "dev4us"}).use(reactotronRedux()).connect();

export default Reactotron;