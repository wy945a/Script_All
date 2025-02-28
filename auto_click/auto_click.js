// 获取所有包含编辑链接的表格单元格
let tdElements = document.querySelectorAll('td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first.ant-table-cell-ellipsis');

if (tdElements.length === 0) {
    console.error('未找到指定类名的表格单元格。');
} else {
    function processTdElement(tdElement, index) {
        // 打印指定的数据值
        printDataValue(tdElement, index);

        // 找到所有的 <a> 标签
        let links = tdElement.querySelectorAll('a');

        // 过滤出文本为“编辑”的链接
        let editLink = Array.from(links).find(link => link.textContent.trim() === '编辑');

        if (editLink) {
            setTimeout(() => {
                console.log(`点击了索引为 ${index} 的编辑链接`);
                editLink.click();

                // 等待编辑表单加载完成（根据实际情况调整等待时间）
                setTimeout(() => {
                    // 使用更具描述性的类名来定位确认按钮
                    let drawerFooter = document.querySelector('.ant-drawer-footer');

                    if (drawerFooter) {
                        let confirmButton = drawerFooter.querySelector('.ant-btn-primary');

                        if (confirmButton) {
                            console.log('找到了确认按钮:', confirmButton);
                            confirmButton.click();

                            // 检查确认按钮是否仍然存在
                            setTimeout(() => {
                                let confirmButtonStillExists = drawerFooter.querySelector('.ant-btn-primary');

                                if (confirmButtonStillExists) {
                                    console.error('确认按钮仍然存在，停止脚本执行。');
                                    return;  // 停止脚本执行
                                } else {
                                    console.log('确认按钮已消失。');

                                    // 如果需要等待保存操作完成再继续，可以添加适当的等待时间
                                    setTimeout(() => {
                                        // 继续处理下一个元素（可选，视具体需求而定）
                                        if (index + 1 < tdElements.length) {
                                            processTdElement(tdElements[index + 1], index + 1);
                                        }
                                    }, 500);  // 根据实际情况调整等待时间
                                }
                            }, 3000);  // 点击确认按钮后等待2秒
                        } else {
                            console.error(`在索引为 ${index} 的项中未找到确认按钮`);
                            // 如果没有找到确认按钮，停止脚本执行
                            return;
                        }
                    } else {
                        console.error('未找到抽屉页脚容器。');
                        return;
                    }
                }, 500);  // 等待编辑表单加载完成的时间
            }, 500 * index);  // 每次点击间隔0.5秒，可根据实际情况调整
        } else {
            console.error(`在索引为 ${index} 的行中未找到编辑链接`);
        }
    }

    // 开始处理第一个元素
    if (tdElements.length > 0) {
        processTdElement(tdElements[0], 0);
    }
}

// 打印指定的数据值
function printDataValue(tdElement, rowIndex) {
    // 根据当前的tdElement定位对应的行并找到数据值
    let tr = tdElement.closest('tr');  // 获取当前td所在的行
    if (tr) {
        // 假设数据值位于第二列（即第二个td元素）
        let dataCell = tr.querySelector('td:nth-child(2)');

        if (dataCell) {
            console.log(`第 ${rowIndex} 行的数据值为:`, dataCell.textContent.trim());
        } else {
            console.error(`在第 ${rowIndex} 行中未找到数据单元格`);
        }
    } else {
        console.error(`未找到与索引为 ${rowIndex} 的td元素对应的行`);
    }
}