import React from 'react';
import styled from 'styled-components';
import Input from './Input';

const FormContainer = styled.form`
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
  background-color: #f4f4f4;
  border-radius: 4px;
`;

const SubmitButton = styled.button`
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  &:hover {
    background-color: #0056b3;
  }
`;

interface FormProps {
    formData: FormData;
    handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
    handleSubmit: (event: React.FormEvent<HTMLFormElement>) => void;
}

const Form: React.FC<FormProps> = ({ formData, handleChange, handleSubmit }) => {
    return (
        <FormContainer onSubmit={handleSubmit}>
            <Input name="INT_SQFT" label="INT_SQFT" value={formData.INT_SQFT} onChange={handleChange} required />
            <Input name="N_BEDROOM" label="N_BEDROOM" value={formData.N_BEDROOM} onChange={handleChange} required />
            <Input name="N_BATHROOM" label="N_BATHROOM" value={formData.N_BATHROOM} onChange={handleChange} required />
            <Input name="N_ROOM" label="N_ROOM" value={formData.N_ROOM} onChange={handleChange} required />
            <Input name="AREA" label="AREA" value={formData.AREA} onChange={handleChange} required />
            <Input name="DIST_MAINROAD" label="DIST_MAINROAD" value={formData.DIST_MAINROAD} onChange={handleChange} required />
            <Input name="PARK_FACIL" label="PARK_FACIL" value={formData.PARK_FACIL} onChange={handleChange} required />
            <Input name="BUILDTYPE" label="BUILDTYPE" value={formData.BUILDTYPE} onChange={handleChange} required />
            <Input name="STREET" label="STREET" value={formData.STREET} onChange={handleChange} required />
            <Input name="MZZONE" label="MZZONE" value={formData.MZZONE} onChange={handleChange} required />
            <Input name="QS_ROOMS" label="QS_ROOMS" value={formData.QS_ROOMS} onChange={handleChange} required />
            <Input name="QS_BATHROOM" label="QS_BATHROOM" value={formData.QS_BATHROOM} onChange={handleChange} required />
            <Input name="QS_BEDROOM" label="QS_BEDROOM" value={formData.QS_BEDROOM} onChange={handleChange} required />
            <Input name="QS_OVERALL" label="QS_OVERALL" value={formData.QS_OVERALL} onChange={handleChange} required />
            <Input name="COMMIS" label="COMMIS" value={formData.COMMIS} onChange={handleChange} required />

            <SubmitButton type="submit">Predict Price</SubmitButton>
        </FormContainer>
    );
};

export default Form;
