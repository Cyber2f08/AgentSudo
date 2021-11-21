var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var getQuestionsElement = function () {
    var questionsElem = document.querySelector("body > div > div.root-component > div > div > div > div.page-container.in-quiz > div.screen.screen-game > div.transitioner.transitioner-component > div > div > div > div > div > div.options-container > div");
    if (!questionsElem)
        throw new Error("Unable to retreive questions list element");
    return questionsElem;
};
var changeElementOpacity = function (elem) {
    elem.style.opacity = "20%";
};
var highlightAnswers = function (question) {
    var questionsElem = getQuestionsElement();
    var arr = Array.prototype.slice.call(questionsElem.children);
    if (Array.isArray(question.structure.answer) && question.structure.answer.length < 1 && question.structure.options) {
        var answers = question.structure.options.map(function (option) { return option.text; }).join(" or ");
        alert(answers);
        return;
    }
    arr.filter(function (e) {
        if (Array.isArray(question.structure.answer) && question.structure.answer.length > 0) {
            return !(question.structure.answer.some(function (ansID) { return e.__vue__.optionData.actualIndex === ansID; }));
        }
        else if (typeof question.structure.answer == "number") {
            return e.__vue__.optionData.actualIndex !== question.structure.answer;
        }
        else {
            console.error("Fail detecting type of question: ", question);
        }
    }).forEach(changeElementOpacity);
};
var getQuestionInfo = function () {
    var rootObject = document.querySelector("body > div");
    if (!rootObject)
        throw new Error("Could not retrieve root object");
    var vue = rootObject.__vue__;
    return {
        roomHash: vue.$store._vm._data.$$state.game.data.roomHash,
        playerId: vue.$store._vm._data.$$state.game.player.playerId,
        quizID: vue.$store._vm._data.$$state.game.data.quizId,
        roomCode: vue.$store._vm._data.$$state.game.data.roomCode,
        questionID: vue.$store._vm._data.$$state.game.questions.currentId,
    };
};
var getRoomHash = function () {
    var rootObject = document.querySelector("body > div");
    if (!rootObject)
        throw new Error("Could not retrieve root object");
    var vue = rootObject.__vue__;
    return vue.$store._vm._data.$$state.game.data.roomHash;
};
var msg = "%c \n        Script is been created is on production...\n        Created by @Cyber2f08\n      ";
var wel = "%c\n[Purify] Scripts initialized..\n[Purify] Running cheat code\n[Purify] Happy hacking\n[Purify] Make with love from Cyber2f08\n      ";
(function () { return __awaiter(void 0, void 0, void 0, function () {
    var quiz, lastQuestionID;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                console.log(msg, "color: red;");
                console.log("Initiating external scripts....", "color: yellow;");
                console.log(wel, "color: yellow");
                return [4 /*yield*/, fetch("https://quizizz.com/_api/main/game/".concat(getRoomHash()))];
            case 1: return [4 /*yield*/, (_a.sent()).json()];
            case 2:
                quiz = _a.sent();
                lastQuestionID = undefined;
                setInterval(function () {
                    var questionInfo = getQuestionInfo();
                    if (questionInfo.questionID !== lastQuestionID) {
                        for (var _i = 0, _a = quiz.data.questions; _i < _a.length; _i++) {
                            var q = _a[_i];
                            if (questionInfo.questionID === q._id) {
                                highlightAnswers(q);
                                console.log("[Purify] Answer highlighted... ");
                                console.log("[Purify] Baking answer to list..");
                                console.log({ q: q });
                                lastQuestionID = questionInfo.questionID;
                            }
                            console.log("[Purify] Done the quiz is done!");
                            console.log("[Purify] Happy day for you, thank you. Love from Cyber2f08");
                        }
                    }
                }, 500);
                return [2 /*return*/];
        }
    });
}); })();
export {};
