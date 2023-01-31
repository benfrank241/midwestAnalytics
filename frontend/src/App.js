import Navbar from "./Navbar"
import Baseball from "./pages/Baseball"
import Home from "./pages/Home"
import Football from "./pages/Football"
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/baseball" element={<Baseball />} />
          <Route path="/football" element={<Football />} />
        </Routes>
      </div>
    </>
  )
}

export default App