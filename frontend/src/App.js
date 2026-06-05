import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "./components/card";
import { Button } from "./components/button";
import { Input } from "./components/inout"; // Fixed typo: 'inout' -> 'input'
import { Label } from "./components/label";
import { FaComment } from "react-icons/fa"; // Chat icon from react-icons
import './App.css';

const PatientCaseFinder = () => {
  const [symptoms, setSymptoms] = useState({
    symptom1: "",
    symptom2: "",
    symptom3: "",
    symptom4: "",
  });
  const [age, setAge] = useState("");
  const [prediction, setPrediction] = useState(null);
  const [showTreatment, setShowTreatment] = useState(false);
  const [loading, setLoading] = useState(false);
  const [chatResponse, setChatResponse] = useState("");
  const [feverInput, setFeverInput] = useState("");
  const [showChat, setShowChat] = useState(false); // New state to toggle chat visibility

  const handleSymptomChange = (symptom, value) => {
    setSymptoms((prev) => ({
      ...prev,
      [symptom]: value,
    }));
  };

  const handleCheckDisease = async () => {
    try {
      setLoading(true);
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          symptom1: symptoms.symptom1,
          symptom2: symptoms.symptom2,
          symptom3: symptoms.symptom3,
          symptom4: symptoms.symptom4,
          age: age,
        }),
      });

      const data = await response.json();
      if (data.success) {
        setPrediction({
          disease: data.disease,
          confidence: data.confidence,
          ...data.treatment,
        });
        setShowTreatment(false);
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleChatRequest = async () => {
    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: feverInput,
        }),
      });

      const data = await response.json();
      if (data.success) {
        setChatResponse(data.response); // Use the chatbot response
      } else {
        setChatResponse("Sorry, no suggestions available.");
      }
    } catch (error) {
      console.error("Error:", error);
      setChatResponse("Error fetching suggestions.");
    }
  };

  return React.createElement(
    "div",
    { className: "max-w-2xl mx-auto p-4" },
    React.createElement(
      Card,
      null,
      React.createElement(
        CardHeader,
        null,
        React.createElement(
          CardTitle,

        )
      ),
      React.createElement(
        CardContent,
        { className: "space-y-6" },
        // Symptoms Input Section
        React.createElement(
          "div",
          { className: "grid grid-cols-1 md:grid-cols-2 gap-4" },
          Object.keys(symptoms).map((symptom, index) =>
            React.createElement(
              "div",
              { key: symptom, className: "space-y-2" },
              React.createElement(
                Label,
                { htmlFor: symptom, className: "text-sm font-semibold" },
                `Symptom ${index + 1}`
              ),
              React.createElement(Input, {
                id: symptom,
                type: "text",
                placeholder: `Enter symptom ${index + 1}`,
                value: symptoms[symptom],
                onChange: (e) => handleSymptomChange(symptom, e.target.value),
                className: "w-full bg-white input-filled", // Added 'input-filled' class for better visual feedback
              })
            )
          )
        ),
        // Age Input Section
        React.createElement(
          "div",
          { className: "space-y-2" },
          React.createElement(
            Label,
            { htmlFor: "age", className: "text-sm font-semibold" },
            "Patient Age"
          ),
          React.createElement(Input, {
            id: "age",
            type: "number",
            placeholder: "Enter patient age",
            value: age,
            onChange: (e) => setAge(e.target.value),
            className: "w-full bg-white input-filled", // Added 'input-filled' class for better visual feedback
            min: "0",
            max: "120",
          })
        ),
        // Check Disease Button
        React.createElement(
          Button,
          {
            onClick: handleCheckDisease,
            className: "w-full mt-4 flex justify-center",
            disabled: loading || !age || Object.values(symptoms).some((s) => !s),
          },
          loading ? "Checking..." : "Check Disease"
        ),
        // Prediction Results
        prediction &&
          React.createElement(
            "div",
            { className: "space-y-4" },
            React.createElement(
              "div",
              { className: "p-4 bg-blue-50 rounded-lg" },
              React.createElement(
                "h3",
                { className: "font-bold text-lg mb-2" },
                "Predicted Disease:"
              ),
              React.createElement("p", { className: "text-lg" }, prediction.disease),
              React.createElement(
                "p",
                { className: "text-sm text-gray-600 mt-1" },
                `Confidence: ${prediction.confidence}`
              )
            ),
            React.createElement(
              Button,
              {
                onClick: () => setShowTreatment(true),
                className: "w-full flex justify-center",
                variant: "primary",
              },
              "Get Treatment Details"
            ),
            showTreatment &&
              React.createElement(
                "div",
                { className: "p-4 bg-blue-50 rounded-lg shadow-md space-y-3" }, // Changed bg-white-50 to bg-white and added shadow-md
                React.createElement(
                  "h3",
                  { className: "font-bold text-lg mb-2" },
                  "Treatment & Recommendations"
                ),
                React.createElement(
                  "p",
                  null,
                  `Medication: ${prediction.medication}`
                ),
                React.createElement(
                  "p",
                  null,
                  `Cure Methods: ${prediction.cureMethods}`
                ),
                React.createElement(
                  "p",
                  null,
                  `Outcome: ${prediction.outcome}`
                ),
                React.createElement(
                  "p",
                  null,
                  `Nearby Hospital: ${prediction.nearbyHospital}`
                )
              )
          ),
        // Chatbot Section
        React.createElement(
          "div",
          { className: "fixed bottom-16 right-4 z-50" },
          React.createElement(
            "span",
            { className: "text-sm font-bold text-blue-500 animate-blink" },
            "Assistant here!!!"
          ),
          React.createElement(
            Button,
            {
              onClick: () => {
                setShowChat(!showChat);
                if (showChat) {
                  setChatResponse(""); // Clear chat response when closing the chat
                  setFeverInput("");    // Clear input field when closing the chat
                }
              },
              className: "bg-blue-500 text-white rounded-full p-3",
            },
            React.createElement(FaComment, { size: 20 })
          ),
          showChat &&
            React.createElement(
              "div",
              { className: "chat-container active" },
              React.createElement(
                "div",
                { className: "chat-body" },
                feverInput && (
                  React.createElement(
                    "div",
                    { className: "chat-response" },
                    chatResponse
                  )
                )
              ),
              React.createElement(
                "div",
                { className: "chat-footer" },
                React.createElement("input", {
                  type: "text",
                  placeholder: "Enter the disease name...",
                  value: feverInput,
                  onChange: (e) => setFeverInput(e.target.value),
                  className: "w-full text-center py-2",
                }),
                React.createElement(
                  Button,
                  {
                    onClick: handleChatRequest,
                    className: "ml-2",
                  },
                  "Find vegetable, fruits suggestion"
                ),
                React.createElement(
                  Button,
                  {
                    onClick: () => {
                      setChatResponse(""); // Clear chat response
                      setFeverInput("");   // Clear input field
                    },
                    className: "ml-2 bg-red-500 text-white w-full",
                  },
                  "Clear Chat"
                )
              )
            )
        
        
            
        )
      )
    )
  );
};

export default PatientCaseFinder;
