import Navbar from "./Navbar"
import Baseball from "./pages/Baseball"
import Home from "./pages/Home"
import Football from "./pages/Football"
import Basketball from "./pages/Basketball"
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
          <Route path="/basketball" element={<Basketball />} />
        </Routes>
      </div>
    </>
  )
}

export default App