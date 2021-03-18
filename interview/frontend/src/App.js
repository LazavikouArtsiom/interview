import './App.css';
import {BrowserRouter, Route} from 'react-router-dom'
import Header from './components/Header/Header'
import Footer from './components/Footer/Footer'
import Catalog from './components/Catalog/Catalog'

function App() {
  return (
    <BrowserRouter>
      <div className="wrapper">
        <Header />
          <div className='content'>
            <Route path='/catalog' component={Catalog} />
            {/* 
            <Route path='/catalog/slug' component={CatalogItem} />
            <Route path='/about' component={About} />
            <Route path='/contact' component={Contact} /> */}
          </div>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
