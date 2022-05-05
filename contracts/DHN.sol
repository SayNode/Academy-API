// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "OpenZeppelin/openzeppelin-contracts@4.4.2/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor() ERC20("MyTokenDHN", "DHN") {
        _mint(msg.sender, 1000 * 10 ** decimals());
    }
}