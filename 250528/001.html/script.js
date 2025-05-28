// 동기적으로 동작하는 코드
// console.log("hello");
// console.log("world");

// 비동기적으로 동작하는 코드
// setTimeout(() => {
//     console.log("hello");
// }, 1000);
// console.log("world");

// setTimeout(() => {
//     console.log("hello");
// }, 0);
// console.log("world");

// 콜 스택(함수의 호출에 관련된 역할을 하는 후입선출형) 
// 처리 과정

// const 참깨빵 = () => {
//     console.log("Call 참깨빵");
//     순쇠고기패티();
//     console.log("End 참깨빵");   
// }

// const 순쇠고기패티 = () => {
//     console.log("Call 순쇠고기패티");
//     특별한소스();
//     console.log("End 순쇠고기패티");
// };

// const 특별한소스 = () => {
//     console.log("Call 특별한소스");
//     console.log("End 특별한소스");
// };

// 참깨빵();
// console.log("----함수 호출 종료----");

// 1번문제
console.log("시작");
setTimeout(() => console.log("타이머 A"), 100);
setTimeout(() => console.log("타이머 B"), 50);
console.log("중간");
setTimeout(() => console.log("타이머 C"), 0);
console.log("---끝---");  // 시작, 중간, 끝, 타이머c, b, a


// // //2번문제
console.log("준비");

setTimeout(() => {
    console.log("첫번째 작업 완료");
}, 100);

console.log("시작");

setTimeout(() => {
    console.log("두번째 작업 완료");
}, 200);

setTimeout(() => {
    console.log("모든 작업 끝");
}, 300);


//문제3
function 작업A() {
    console.log("작업A 시작");
    setTimeout(() => {
        console.log("작업A 완료");
    }, 150);
}

function 작업B() {
    console.log("작업B 시작");
    setTimeout(() => {
        console.log("작업B 완료");
    }, 100);
}

console.log("프로그램 시작");
작업A();
작업B();
console.log("프로그램 끝");


