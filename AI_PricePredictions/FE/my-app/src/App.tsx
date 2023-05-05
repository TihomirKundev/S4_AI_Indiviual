import React, { useState, ChangeEvent, FormEvent } from 'react';
import axios from 'axios';
import styled from 'styled-components';
import Form from './components/Form';

const Container = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
`;

const Title = styled.h1`
  font-size: 2rem;
  text-align: center;
  margin-bottom: 2rem;
`;

const PredictedPrice = styled.p`
  font-size: 1.5rem;
  text-align: center;
  margin-top: 2rem;
`;

interface FormData {
  INT_SQFT: string;
  // Add the other fields here, e.g.
  // QS_ROOMS: string;
  // ...
}

const App = () => {
  const [formData, setFormData] = useState<FormData>({
    INT_SQFT: '',
    // Initialize the other fields here, e.g.
    // QS_ROOMS: '',
    // ...
  });
  const [predictedPrice, setPredictedPrice] = useState<number | null>(null);

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/predict", formData);
      setPredictedPrice(response.data.price_estimate);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
      <Container>
        <Title>Price Prediction</Title>
        <Form formData={formData} handleChange={handleChange} handleSubmit={handleSubmit} />
        {predictedPrice !== null && (
            <PredictedPrice>
              The predicted price is: <strong>{predictedPrice}</strong>
            </PredictedPrice>
        )}
      </Container>
  );
};

export default App;
