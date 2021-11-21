

import { VueElement, QuizQuestion, QuizInfo } from "./types";

const getQuestionsElement = () => {
  const questionsElem = document.querySelector(
    "body > div > div.root-component > div > div > div > div.page-container.in-quiz > div.screen.screen-game > div.transitioner.transitioner-component > div > div > div > div > div > div.options-container > div"
  );
  if (!questionsElem)
    throw new Error("Unable to retreive questions list element");

  return questionsElem;
};

const changeElementOpacity = (elem: HTMLElement) => {
  elem.style.opacity = "20%";
};

const highlightAnswers = (question: QuizQuestion) => {
  const questionsElem = getQuestionsElement();
  const arr: VueElement[] = Array.prototype.slice.call(questionsElem.children);

  if (Array.isArray(question.structure.answer) && question.structure.answer.length < 1 && question.structure.options) {
    const answers = question.structure.options.map((option) => option.text).join(" or ");
    alert(answers);

    return;
  }

  arr.filter((e) => {
    if (Array.isArray(question.structure.answer) && question.structure.answer.length > 0) {
      return !(question.structure.answer.some((ansID) => e.__vue__.optionData.actualIndex === ansID));
    } else if(typeof question.structure.answer == "number") {
      return e.__vue__.optionData.actualIndex !== question.structure.answer
    } else {
      console.error("Fail detecting type of question: ", question);
    }
  }).forEach(changeElementOpacity);
}

const getQuestionInfo = (): {
  questionID: string;
  roomHash: string;
  playerId: string;
  quizID: string;
  roomCode: string;
} => {
  const rootObject = document.querySelector("body > div") as VueElement | null;
  if (!rootObject) throw new Error("Could not retrieve root object");
  const vue = rootObject.__vue__;

  return { 
    roomHash:   vue.$store._vm._data.$$state.game.data.roomHash, 
    playerId:   vue.$store._vm._data.$$state.game.player.playerId, 
    quizID:     vue.$store._vm._data.$$state.game.data.quizId,
    roomCode:   vue.$store._vm._data.$$state.game.data.roomCode,
    questionID: vue.$store._vm._data.$$state.game.questions.currentId,
  };
};

const getRoomHash = (): string => {
  const rootObject = document.querySelector("body > div") as VueElement | null;
  if (!rootObject) throw new Error("Could not retrieve root object");
  const vue = rootObject.__vue__;

  return vue.$store._vm._data.$$state.game.data.roomHash;
}

const msg = `%c 
        Script is been created is on production...
        Created by @Cyber2f08
      `;
const wel = `%c
        [Purify] Scripts initialized..
        [Purify] Running cheat code
        [Purify] Happy hacking
        [Purify] Make with love from Cyber2f08
      `;


(async () => {
  console.log(msg, "color: red;");
  console.log("Initiating external scripts....", "color: yellow;")
  console.log(wel, "color: yellow")

  const quiz: QuizInfo = await (await fetch(`https://quizizz.com/_api/main/game/${getRoomHash()}`)).json();

  let lastQuestionID: string | undefined = undefined;

  setInterval(() => {
    const questionInfo = getQuestionInfo();
    if (questionInfo.questionID !== lastQuestionID) {
      for (const q of quiz.data.questions) {
        if (questionInfo.questionID === q._id) {
          highlightAnswers(q);
          console.log("[Purify] Answer highlighted... ")
          console.log("[Purify] Initiating bakery of script..")
          console.log({q})
          lastQuestionID = questionInfo.questionID;
        }
      }
    }
  }, 500)

})();