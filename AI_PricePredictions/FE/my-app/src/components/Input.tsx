import React from 'react';
import styled from 'styled-components';

const InputContainer = styled.div`
  margin-bottom: 1rem;
`;

const Label = styled.label`
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
`;

const StyledInput = styled.input`
  display: block;
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
`;

interface InputProps {
    name: string;
    label: string;
    value: string;
    type?: string;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
    required?: boolean;
}

const Input: React.FC<InputProps> = ({
                                         name,
                                         label,
                                         value,
                                         type = 'text',
                                         onChange,
                                         required = false,
                                     }) => {
    return (
        <InputContainer>
            <Label htmlFor={name}>{label}</Label>
            <StyledInput id={name} name={name} type={type} value={value} onChange={onChange} required={required} />
        </InputContainer>
    );
};

export default Input;
