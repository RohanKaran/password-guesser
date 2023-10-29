import React from 'react';
import {Button, Col, Container, Form, InputGroup, Row} from 'react-bootstrap';
import './App.css';
import {VscAccount, VscHubot} from "react-icons/vsc";
import axios from "axios";

function App() {
  const [level, setLevel] = React.useState(1);
  const [prompt, setPrompt] = React.useState("");
  const [promptMessage, setPromptMessage] = React.useState("");
  const [promptShow, setPromptShow] = React.useState(false);
  const [promptResponse, setPromptResponse] = React.useState("");
  const [promptResponseShow, setPromptResponseShow] = React.useState(false);
  const [password, setPassword] = React.useState("");
  const backend = process.env.REACT_APP_BACKEND
  const getResponse = () => {
    if (prompt.trim() === "") return
    setPrompt("")
    setPromptMessage(prompt)
    setPromptShow(true)
    setPromptResponse("...")
    axios.post(`${backend}/response`, {level: level, query: prompt})
      .then(res => {
          setPromptResponse(res.data)
          setPromptResponseShow(true)
        }
      )
      .catch(err => console.log(err))
  }
  const guessPassword = () => {
    if (password.trim() === "") return
    setPassword("")
    axios.post(`${backend}/guess`, {level: level, password: password})
      .then(res => {
        setPromptShow(false)
        setPromptResponseShow(false)
        setLevel(level + 1)
      }
      )
      .catch(err => console.log(err))
  }
  return (
    <div className="App" data-bs-theme="dark" style={{wordWrap: "break-word"}}>
      <div id={"passed"} hidden={level >= 1 && level <= 3}>
        <h1 className={"mt-5"}>Congratulations! you've passed all the levels.</h1>
        <Button variant="primary" onClick={() => window.location.reload()}>Restart</Button>
      </div>
      <div id={"main"} hidden={level < 1 || level > 3}>
        <h1 className={"mt-5"}>Password Guesser</h1>
        <h3 className={"mb-5"}>Level {level}</h3>
        <Container>
          <div align={"right"} className={"mb-5"} hidden={!promptShow}>
            <Row style={{margin: 0}}>
              <Col/>
              <Col sm={promptMessage.length > 50 ? 9 : promptMessage.length > 20 ? 6 : 4} style={{
                backgroundColor: "blueviolet",
                borderRadius: "5px",
                flex: "0 0 auto",
                textAlign: "right"
              }}>
                <div className={"mb-2 mt-2"}>{promptMessage}</div>
              </Col>
              <Col sm={1}><VscAccount size={45}/></Col>
            </Row>
          </div>
          <div align={"left"} hidden={!promptResponseShow}>
            <Row style={{margin: 0}}>
              <Col sm={1}><VscHubot size={50}/></Col>
              <Col sm={promptResponse.length > 50 ? 9 : promptResponse.length > 20 ? 6 : 4}
                   style={{
                     backgroundColor: "darkcyan",
                     borderRadius: "5px",
                     flex: "0 0 auto",
                     textAlign: "left"
                   }}>
                <div className={"mb-2 mt-2"}>{promptResponse}</div>
              </Col>
              <Col/>
            </Row>
          </div>
          <InputGroup className={"mt-5 mb-5"}>
            <Form.Control type={"textarea"} value={prompt} onChange={e => setPrompt(e.target.value)}/>
            <Button type={"submit"} variant="primary" onClick={() => getResponse(prompt)}>Send</Button>
          </InputGroup>
          <Container style={{width: "50%", marginTop: '5rem'}}>
            <h4 className={"mt-5"}>Check password for level {level}</h4>
            <InputGroup className={"mt-3"}>
              <Form.Control type={"textarea"} value={password} onChange={e => setPassword(e.target.value)}/>
              <Button type={"submit"} variant="success" onClick={() => guessPassword()}>Check</Button>
            </InputGroup>
          </Container>
        </Container>
      </div>
    </div>
  );
}

export default App;
